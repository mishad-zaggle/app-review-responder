
---

# 🤖 Smart App Review Responder

An AI-powered tool to automatically analyze app reviews, determine sentiment, fetch relevant FAQs using semantic search, and generate contextual, human-like responses using OpenAI. The project features a simple **Streamlit UI** for interactive usage.

---

## 📦 Features

- 🔍 **Sentiment Analysis** using OpenAI's GPT
- 💬 **Response Generation** based on custom prompt templates
- 📚 **Semantic FAQ Search** using FAISS & OpenAI embeddings
- 🔄 **Redis-powered Chat History**
- 🌐 **Streamlit Web App** for interactive review response generation
- ✅ Support for Positive, Neutral, and Negative review handling

---

## 📂 Project Structure

```
├── app_review_responder.py         # Streamlit frontend
├── initializers/
│   ├── constants.py                # App-wide constants
│   └── prompts/prompt_templates.py # Predefined prompt templates
├── utils/
│   ├── openai_utils.py             # Embeddings, FAISS, OpenAI logic
│   └── common_utils.py             # Redis, CSV loading, chat history
├── datasets/
│   └── training/                   # Reference Datasets for Prompt Enhancements
├── .env                            # OpenAI key and config
├── requirements.txt                # Dependencies
└── README.md                       # Project Information
```

---

## 🚀 How It Works

1. **User Review Input**: Provided via the **Streamlit web app**.
2. **Sentiment Classification**: Done via GPT with predefined prompts.
3. **FAQ Semantic Search**: Using FAISS index and OpenAI embeddings.
4. **Response Generation**: Prompts are customized based on sentiment + FAQ context and passed to GPT.
5. **Redis Chat History**: Used for generating context-aware conversations.
6. **Streamlit Output**: Response is displayed instantly in the UI.

---

## 🧠 Prompt Logic

| Scenario                     | Prompt Template               |
|-----------------------------|-------------------------------|
| Positive rating & sentiment | `POSITIVE_RESPONSE_PROMPT`    |
| Negative sentiment          | `NEGATIVE_RESPONSE_PROMPT`    |
| Neutral/unknown             | `NEUTRAL_RESPONSE_PROMPT`     |

---

## 🖥️ Streamlit UI

To run the app:

```bash
streamlit run app.py
```

Once running, go to [http://localhost:8501](http://localhost:8501) in your browser.

The UI allows:
- Typing or pasting a review
- Selecting a star rating
- Submitting for an AI-generated response
- Viewing the result immediately

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-org/review-responder.git
```

### 2. Create `.env`

```env
OPENAI_API_KEY=your-openai-key-here
REDIS_HOST=localhost
REDIS_PORT=6379
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare FAQ Data

Ensure your `faq_dataset.csv` exists and looks like:

```csv
User Query,Product Response
"How do I reset my password?", "Go to settings > account > reset password."
```

The system will:
- Generate embeddings if missing
- Create a FAISS index automatically
- FAQ Index and FAQ Index Files fill be generated in the first time usage and then will be saved

---

## 📚 Tech Stack

- ⚙️ **Python 3.10+**
- 💬 **OpenAI (Chat & Embeddings)**
- 🧠 **FAISS** – Efficient vector similarity search
- 🔁 **Redis** – Stores per-user chat history
- 🌐 **Streamlit** – Web frontend interface
- 🧾 **Pandas, NumPy, dotenv, decouple**

---

## 🧪 Sample Usage (via code)

```python
from utils.openai_utils import generate_response_for_review

response = generate_response_for_review(
    review_text="I can't log in anymore after updating the app.",
    star_rating=1,
    user_id="user_123"
)
print(response)
```

---

## 📸 UI Preview

## 📷 Screenshots

## User ID Input
<img width="1483" alt="Screenshot 2025-04-13 at 20 44 12" src="https://github.com/user-attachments/assets/fa45da6b-d16b-46d7-a025-8f7d32062ea2" />

## Share Feedback Section
<img width="1486" alt="Screenshot 2025-04-13 at 20 17 26" src="https://github.com/user-attachments/assets/8a564f4b-8bd1-484c-9677-24a33a0caf9c" />

## Sample Response
<img width="1486" alt="Screenshot 2025-04-13 at 20 17 26" src="https://github.com/user-attachments/assets/1d13598c-2995-4adc-a6ff-4dc436632e04" />

## Follow-Up / Reply Section
<img width="1494" alt="Screenshot 2025-04-13 at 20 18 57" src="https://github.com/user-attachments/assets/08891a87-5a28-47ca-a581-d786f645142c" />

## Negative Review Coversation History
![screencapture-localhost-8501-2025-04-13-20_32_42](https://github.com/user-attachments/assets/b4fe072b-e93a-43e5-b77b-2d408b9f7a4c)

## Positive Review Coversation History









