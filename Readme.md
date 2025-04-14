
---

# 🤖 Smart App Review Responder

Demo: [Click here to view the video](https://zaggleprep-my.sharepoint.com/:v:/g/personal/misha_dey_zaggle_in/ESsngDxBHJBDrNVoFbV9acsBQF1mJECG_NE2SzQn7mA7rg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=Srykk0)


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
<img width="1512" alt="Screenshot 2025-04-13 at 20 16 59" src="https://github.com/user-attachments/assets/80785a1d-63d1-4915-a570-bc758996b72b" />

## Sample Response
<img width="1486" alt="Screenshot 2025-04-13 at 20 17 26" src="https://github.com/user-attachments/assets/1d13598c-2995-4adc-a6ff-4dc436632e04" />

## Follow-Up / Reply Section
<img width="1494" alt="Screenshot 2025-04-13 at 20 18 57" src="https://github.com/user-attachments/assets/08891a87-5a28-47ca-a581-d786f645142c" />

## Responses to Google Play/App Store Reviews - Negative Review Conversation History
![screencapture-localhost-8501-2025-04-13-20_54_11](https://github.com/user-attachments/assets/fc3a0450-bbdf-423c-b62b-693ed952e0d0)

## Responses to Google Play/App Store Reviews - Positive Review Conversation History
![screencapture-localhost-8501-2025-04-13-21_07_41](https://github.com/user-attachments/assets/41f31350-190e-425d-992d-13ef3a203ced)

## Responses to Google Play/App Store Reviews - Neutral / Random Reviews Conversion
![screencapture-localhost-8501-2025-04-13-21_12_08](https://github.com/user-attachments/assets/acca5d2a-470a-4afc-86b7-b0a91bf097b1)

## Google Play v/s Agent Response Comparision
## Negative Reviews:

## Sample 1:
### Google Play Response:
<img width="885" alt="Screenshot 2025-04-14 at 12 45 13" src="https://github.com/user-attachments/assets/00bceae1-c10b-4ce2-8638-44f61c70567b" />

### Agent Response:
<img width="1464" alt="Screenshot 2025-04-14 at 12 47 08" src="https://github.com/user-attachments/assets/f6e44324-ad92-4bd1-944f-cbc8b660f5a3" />

## Sample 2:
### Google Play Response:
<img width="774" alt="Screenshot 2025-04-14 at 12 48 43" src="https://github.com/user-attachments/assets/319242d4-b883-4c98-8588-3cd0bd00455f" />
### Agent Response:
<img width="1474" alt="Screenshot 2025-04-14 at 12 49 26" src="https://github.com/user-attachments/assets/70ee193d-04ef-4318-9487-29abc565b7ff" />

## Sample 3:
### Google Play Response:
<img width="715" alt="Screenshot 2025-04-14 at 12 52 07" src="https://github.com/user-attachments/assets/580eea9a-14db-48d1-9f1e-421694ea093d" />

### Agent Response:
<img width="1475" alt="Screenshot 2025-04-14 at 12 53 29" src="https://github.com/user-attachments/assets/201e8a4c-c3d0-4ed3-b5be-875991b9bc4b" />

## Positive Reviews:
## Sample 1:
### Google Play Response:
<img width="690" alt="Screenshot 2025-04-14 at 12 57 25" src="https://github.com/user-attachments/assets/8ba5f868-a546-4626-899e-49c0fee9c89f" />

### Agent Response:
<img width="1442" alt="Screenshot 2025-04-14 at 12 58 18" src="https://github.com/user-attachments/assets/9d752d65-0deb-4917-a7ee-1bb517b391cb" />

## Sample 2:
### Google Play Response:
<img width="849" alt="Screenshot 2025-04-14 at 12 59 29" src="https://github.com/user-attachments/assets/c317db57-bf62-463d-a145-8c1ff363299f" />

### Agent Response:
<img width="1473" alt="Screenshot 2025-04-14 at 12 59 50" src="https://github.com/user-attachments/assets/21f94cba-2912-45fa-b2f6-8ebb07711c4c" />


## Agent Responding to Reviews in Other Languages:
### Sample 1
<img width="1471" alt="Screenshot 2025-04-14 at 14 22 38" src="https://github.com/user-attachments/assets/fb5b2001-8dc6-4dd5-9d16-4cae612914a1" />
### Sample 2
<img width="1194" alt="Screenshot 2025-04-14 at 14 23 30" src="https://github.com/user-attachments/assets/4d56ca18-0073-49f8-8246-82708f849c36" />

