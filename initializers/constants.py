# OPENAI
TEXT_EMBEDDING_MODEL = "text-embedding-3-small"
OPEN_AI_CHAT_MODEL = "gpt-4o"

# DATATSET
FAQ_DATASET_PATH = 'datasets/zaggle_faq_dataset.csv'
FAQ_EMBEDDINGS_PATH = 'datasets/faq_embeddings.csv'
FAQ_INDEX_PATH = 'datasets/faq_index.faiss'
USER_QUERY_FIELD = 'User Query'
PRODUCT_RESPONSE_FIELD = 'Product Responses'

# STATIC DATA
NEUTRAL_SENTIMENT = 'Neutral'
POSITIVE_SENTIMENT = 'Positive'
NEGATIVE_SENTIMENT = 'Negative'
POSITIVE_RATING_LOWER_LIMIT = 4
NUMBER_OF_FAQ_RESULTS = 1

# USER / SESSION CONSTANTS
THREAD_ID = "1"

# UI
# CSS STYLES
APP_REVIEW_RESPONDER_STYLE = """
    <style>
        .main {
            background-color: #fafafa !important;
        }
        .title-style {
            font-size: 36px;
            font-weight: bold;
            color: #d32f2f; /* red for heading to match button, optional */
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 18px;
            color: #5f6368;
            margin-bottom: 20px;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton button {
            background-color: #d32f2f !important;  /* red */
            color: white !important;
            border-radius: 5px;
            padding: 12px 24px;
            font-size: 16px;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #b71c1c !important;  /* darker red on hover */
        }
        .review-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 15px;
        }
        .review-card .ai-response {
            background-color: #f1f1f1;
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            color: #333333;
        }
        .review-card .user-message {
            font-weight: bold;
            color: #d32f2f;
        }
        .review-card .ai-message {
            color: #4caf50;
        }
        .review-card .review-text {
            font-size: 16px;
            color: #333333;
        }
    </style>
"""

# Titles and Headers
STAR_OPTIONS = {
    "⭐⭐⭐⭐⭐ Excellent": 5,
    "⭐⭐⭐⭐ Good": 4,
    "⭐⭐⭐ Average": 3,
    "⭐⭐ Needs Improvement": 2,
    "⭐ Very Poor": 1,
}
TITLE_TEXT = "💬 Share Your Feedback"
SUBTITLE_TEXT = "We'd love to hear your experience with Zaggle. Rate us and share your thoughts — our smart assistant will respond shortly!"
USER_ID_INPUT = "Your User ID"
USER_ID_LABEL = "🙋 Tell us who you are"
USER_ID_WARNING = "⚠️ Please enter your User ID to continue."
USER_ID_PLACEHOLDER = "Enter your User ID"
FEEDBACK_LABEL = "📝 Your Feedback"
RATE_LABEL = "🌟 How would you rate us?"
SUBMIT_BUTTON_TEXT = "💡 Submit Feedback"
NO_REVIEW_WARNING = "⚠️ Please write a review before submitting."
SUCCESS_RESPONSE = "✅ Here's our response:"
PREVIOUS_CONVERSATIONS_TITLE = "🧾 CHAT HISTORY"
FOLLOW_UP_PROMPT = "💬 Want to add more?"
FOLLOW_UP_INPUT_PLACEHOLDER = "Type your message here..."
CONTINUE_BUTTON_TEXT = "🔄 Continue"
USER_REVIEW_LABEL = "🧑 You:"
AI_RESPONSE_LABEL = "🤖 Zaggle:"
SHARE_YOUR_FEEDBACK = "💬 Share your experience"
REVIEW_LABEL = "Write your review here..."
ENTER_MESSAGE_WARNING = "⚠️ Please enter a message."
GENERATING_RESPONSE = "✍️ Generating response..."