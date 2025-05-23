import pandas
import redis
import json
from dotenv import load_dotenv
from decouple import config

# Load environment variables
load_dotenv()

# Setup Redis connection
redis_config = redis.StrictRedis(
    host=config('REDIS_HOST', default='localhost'),
    port=config('REDIS_PORT', default=6379),
    db=config('REDIS_DB', default=0),
    decode_responses=True
)


"""
Loads the dataset from a CSV file and returns it as a pandas DataFrame.
@param file_path: The path to the CSV file containing the dataset.
@return: A pandas DataFrame containing the dataset.
"""
def load_dataset(file_path):
    data_frame = pandas.read_csv(file_path)
    return data_frame

"""
Store chat history in Redis with a 1-hour expiration.
@param user_id: The unique identifier for the user.
@param query: The user's query.
@param response: The response generated by the system.
"""
def store_chat_history(user_id, query, response, thread_id='1'):
    key = f"chat_history:{user_id}:{thread_id}"
    history = redis_config.get(key)
    
    if history:
        history = json.loads(history)
    else:
        history = []

    history.append({ "user": query, "assistant": response })
    redis_config.setex(key, 3600, json.dumps(history))

"""
Fetch chat history from Redis.
@param user_id: The unique identifier for the user.
@return: The chat history for the user, or None if not found.
"""
def fetch_chat_history(user_id, thread_id='1'):
    key = f"chat_history:{user_id}:{thread_id}"
    history = redis_config.get(key)
    return json.loads(history) if history else []