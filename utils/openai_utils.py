"""
This module is responsible for interacting with OpenAI's API to fetch embeddings for given text inputs.
"""

import os
import openai
import numpy
from dotenv import load_dotenv
from decouple import config
import faiss as FAISS
import ast
import pdb

from utils.common_utils import load_dataset, store_chat_history, fetch_chat_history
from initializers.prompts.prompt_templates import (
    SENTIMENT_ANALYSIS_PROMPT,
    POSITIVE_RESPONSE_PROMPT,
    NEGATIVE_RESPONSE_PROMPT,
    NEUTRAL_RESPONSE_PROMPT
)

from initializers.constants import (
    TEXT_EMBEDDING_MODEL,
    OPEN_AI_CHAT_MODEL,
    FAQ_DATASET_PATH,
    FAQ_EMBEDDINGS_PATH,
    FAQ_INDEX_PATH,
    NUMBER_OF_FAQ_RESULTS,
    POSITIVE_SENTIMENT,
    NEUTRAL_SENTIMENT,
    NEGATIVE_SENTIMENT,
    USER_QUERY_FIELD,
    PRODUCT_RESPONSE_FIELD,
    POSITIVE_RATING_LOWER_LIMIT
)


"""
Initialize the OpenAI API with the provided API key.
"""
load_dotenv() 
openai.api_key = config('OPENAI_API_KEY')


"""
Generates embeddings for the FAQ dataset and saves them to a CSV file.
@note: The FAQ dataset is loaded from a CSV file, and the embeddings are added to the DataFrame.
@return: A pandas DataFrame containing the FAQ dataset with embeddings.
"""
def generate_faq_database_embeddings():
    faq_dataframe = load_dataset(FAQ_DATASET_PATH)
    faq_dataframe['embedding'] = faq_dataframe[USER_QUERY_FIELD].apply(lambda input_text: fetch_embedded_text(input_text))
    return faq_dataframe


"""
Fetches the embedding for a given text input using OpenAI's API.
@param input_text: The text input for which to fetch the embedding.
@return: The embedding for the input text.
"""
def fetch_embedded_text(input_text):
    result = openai.embeddings.create(
        model=TEXT_EMBEDDING_MODEL,
        input=input_text
    )
    return result.data[0].embedding


"""
Builds or loads a FAISS vector index for the FAQ dataset using precomputed OpenAI embeddings.

This function does the following:
1. Loads the FAQ dataset along with precomputed text embeddings from a CSV file, or generates them if not present.
2. Builds a FAISS index using the embeddings, or loads a previously saved FAISS index from disk.
3. Returns both the FAISS index and the associated FAQ DataFrame for similarity search.

Returns:
    faiss_index (faiss.Index): The FAISS vector index for the FAQ embeddings.
    faq_data_frame (DataFrame): The FAQ dataset with corresponding text embeddings.
"""
def build_faq_faiss_vector_index():
    # Loads or generated the FAQ dataset with embeddings.
    if os.path.exists(FAQ_EMBEDDINGS_PATH):
        faq_data_frame = load_dataset(FAQ_EMBEDDINGS_PATH)
        faq_data_frame['embedding'] = faq_data_frame['embedding'].apply(ast.literal_eval)
    else:
        faq_data_frame = generate_faq_database_embeddings()
        faq_data_frame.to_csv(FAQ_EMBEDDINGS_PATH, index=False)

    
    # Loads or generates the FAISS index.
    if os.path.exists(FAQ_INDEX_PATH):
        faiss_index = FAISS.read_index(FAQ_INDEX_PATH)
    else:
        embedding_dimension = len(faq_data_frame['embedding'][0])
        faiss_index = FAISS.IndexFlatL2(embedding_dimension)
        faq_embeddings = numpy.array(faq_data_frame['embedding'].tolist()).astype('float32')
        faiss_index.add(faq_embeddings)
        FAISS.write_index(faiss_index, FAQ_INDEX_PATH)
    return faiss_index, faq_data_frame


"""
Generates a chat completion using OpenAI's API.
@note: The chat completion is generated using a specific prompt format.
@param prompt: The prompt to send to the OpenAI API.
@return: The generated chat completion response.
"""
def openai_chat_completion(prompt, history = []):
    messages = history.copy()
    messages.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create( model = OPEN_AI_CHAT_MODEL, messages = messages )
    return response.choices[0].message.content


"""
Sentiment analysis using OpenAI's API.
@note: The sentiment analysis is performed using a specific prompt format.
@param input_text: The text input for which to classify the sentiment.
@return: The sentiment classification result (Positive or Negative).
"""
def classify_sentiment(input_text):
    prompt = SENTIMENT_ANALYSIS_PROMPT + input_text
    sentiment =  openai_chat_completion(prompt)
    return sentiment


"""
Search the FAQ database for negative reviews
@note: The search is performed using the FAISS index for efficient similarity search.
@param query: The query text to search for.
@param faiss_index: The FAISS index for the FAQ dataset.
@param faq_dataframe: The FAQ dataset with embeddings.
@return: A list of relevant FAQ answers.
"""
def search_faq_database_for_negative_reviews(query, faiss_index, faq_dataframe):
    embedded_text = fetch_embedded_text(query)
    query_vector = numpy.array([embedded_text]).astype('float32')
    _, indices = faiss_index.search(query_vector, NUMBER_OF_FAQ_RESULTS)
    relevant_faq = faq_dataframe.iloc[indices[0]][PRODUCT_RESPONSE_FIELD].tolist()
    return relevant_faq


"""
Formats the chat history for OpenAI's API.
@note: The chat history is formatted as a list of messages with roles (user and assistant).
@param history: The chat history to format.
@return: A list of formatted messages for OpenAI's API.
"""
def format_history_for_openai(history):
    messages = []
    for entry in history:
        messages.append({"role": "user", "content": entry["user"]})
        messages.append({"role": "assistant", "content": entry["assistant"]})
    return messages


"""
Fetches the appropriate prompt based on the review sentiment and star rating.
@param review_text: The review text to analyze.
@param star_rating: The star rating of the review.
@param sentiment: The sentiment classification result (Positive or Negative).
@return: The appropriate prompt for generating a response.
"""
def fetch_prompt(star_rating, sentiment):
    if star_rating >= POSITIVE_RATING_LOWER_LIMIT and sentiment == POSITIVE_SENTIMENT:
        prompt = POSITIVE_RESPONSE_PROMPT
    elif sentiment == NEGATIVE_SENTIMENT:
        prompt = NEGATIVE_RESPONSE_PROMPT
    else:
        prompt = NEUTRAL_RESPONSE_PROMPT
    return prompt


"""
Generates a response to a user query using OpenAI's API.
@param review_text: The review text to analyze.
@param star_rating: The star rating of the review.
@param user_id: The unique identifier for the user.
@param thread_id: The thread ID for the chat history.
@return: The generated response based on the review sentiment.
"""
def generate_response_for_review(review_text, star_rating, user_id, thread_id='1'):
    review_text = f" (Star Rating: {star_rating} out of 5). " + review_text
    
    # Classify the sentiment of the review
    sentiment = classify_sentiment(review_text)
    history = format_history_for_openai(fetch_chat_history(user_id, thread_id))

    # Search the FAQ database for relevant answers
    faiss_index, faq_dataframe = build_faq_faiss_vector_index()
    relevant_faqs = search_faq_database_for_negative_reviews(review_text, faiss_index, faq_dataframe)
    relevant_faqs = "\n".join([f"- {faq}" for faq in relevant_faqs])
    
    # Generate a response based on the sentiment and star rating
    prompt = fetch_prompt(star_rating, sentiment)
    prompt = prompt + f"\n\n{relevant_faqs}\n\nUser Review:\n{review_text}\n\nRespond:"
    response = openai_chat_completion(prompt, history).strip() 
    
    # Store the chat history in Redis
    store_chat_history(user_id, review_text, response)
    return response