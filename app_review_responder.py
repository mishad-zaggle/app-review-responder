import streamlit
from utils.openai_utils import generate_response_for_review, fetch_chat_history
from initializers.constants import (
    APP_REVIEW_RESPONDER_STYLE,
    THREAD_ID,
    TITLE_TEXT,
    SUBTITLE_TEXT,
    USER_ID_INPUT,
    USER_ID_LABEL,
    USER_ID_WARNING,
    USER_ID_PLACEHOLDER,
    FEEDBACK_LABEL,
    RATE_LABEL,
    SUBMIT_BUTTON_TEXT,
    NO_REVIEW_WARNING,
    PREVIOUS_CONVERSATIONS_TITLE,
    FOLLOW_UP_PROMPT,
    FOLLOW_UP_INPUT_PLACEHOLDER,
    CONTINUE_BUTTON_TEXT,
    USER_REVIEW_LABEL,
    AI_RESPONSE_LABEL,
    STAR_OPTIONS,
    SHARE_YOUR_FEEDBACK,
    REVIEW_LABEL,
    ENTER_MESSAGE_WARNING,
    GENERATING_RESPONSE
)

# ---------- PAGE CONFIGURATION ----------
streamlit.set_page_config(page_title="Zaggle Review Responder", page_icon="💬", layout="wide")

# ---------- STYLING ----------
streamlit.markdown(APP_REVIEW_RESPONDER_STYLE, unsafe_allow_html=True)

# ---------- TITLE ----------
streamlit.markdown(f"<h1 class='title-style'>{TITLE_TEXT}</h1>", unsafe_allow_html=True)
streamlit.markdown(f"<p class='subtitle'>{SUBTITLE_TEXT}</p>", unsafe_allow_html=True)
streamlit.markdown("---")

# ---------- SESSION INIT ----------
if "user_id" not in streamlit.session_state:
    streamlit.session_state["user_id"] = ""

if "chat_history" not in streamlit.session_state:
    streamlit.session_state.chat_history = []

# ---------- USER ID INPUT ----------
streamlit.markdown(f"### {USER_ID_LABEL}")
user_id_input = streamlit.text_input(USER_ID_INPUT, value=streamlit.session_state["user_id"], placeholder=USER_ID_PLACEHOLDER)
streamlit.session_state["user_id"] = user_id_input.strip()

# ---------- GUARD CLAUSE ----------
if not streamlit.session_state["user_id"]:
    streamlit.warning(USER_ID_WARNING)
    streamlit.stop()

# ---------- FETCH CHAT HISTORY ----------
if not streamlit.session_state.chat_history:
    streamlit.session_state.chat_history = fetch_chat_history(streamlit.session_state["user_id"], THREAD_ID) or []

# ---------- INPUT SECTION ----------
streamlit.subheader(FEEDBACK_LABEL)

col1, col2 = streamlit.columns([1, 3])
with col1:
    streamlit.markdown(f"#### {RATE_LABEL}")
    star_options = STAR_OPTIONS
    selected_star = streamlit.radio("", list(star_options.keys()), horizontal=False)
    star_rating = star_options[selected_star]

with col2:
    review_text = streamlit.text_area(SHARE_YOUR_FEEDBACK, height=200, placeholder=REVIEW_LABEL)

streamlit.markdown("---")

# ---------- GENERATE RESPONSE ----------
if streamlit.button(SUBMIT_BUTTON_TEXT):
    if not review_text.strip():
        streamlit.warning(NO_REVIEW_WARNING)
    else:
        with streamlit.spinner("🧠 Analyzing your feedback..."):
            response = generate_response_for_review(review_text, star_rating, streamlit.session_state["user_id"], THREAD_ID)
            streamlit.session_state.chat_history.append({"user": review_text, "assistant": response})
            streamlit.success(AI_RESPONSE_LABEL)
            streamlit.markdown(
                f"""
                <div class='review-card'>
                    <div class="review-text">{response}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------- CHAT DISPLAY + FOLLOW-UP ----------
if len(streamlit.session_state.chat_history) > 0:
    streamlit.markdown(f"### {PREVIOUS_CONVERSATIONS_TITLE}")

    for idx, message in enumerate(streamlit.session_state.chat_history):
        streamlit.markdown(
            f"""
            <div class='review-card'>
                <div class="user-message">{USER_REVIEW_LABEL}</div>
                <div class="review-text">{message['user']}</div>
                <div class="ai-response">
                    {AI_RESPONSE_LABEL} </br> {message['assistant']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if idx == len(streamlit.session_state.chat_history) - 1:
            streamlit.markdown(f"### {FOLLOW_UP_PROMPT}")
            user_follow_up = streamlit.text_input("Add a follow-up or ask a question:", key=f"followup_{idx}", placeholder=FOLLOW_UP_INPUT_PLACEHOLDER)

            if streamlit.button(CONTINUE_BUTTON_TEXT, key=f"continue_{idx}"):
                if not user_follow_up.strip():
                    streamlit.warning(ENTER_MESSAGE_WARNING)
                else:
                    with streamlit.spinner(GENERATING_RESPONSE):
                        response = generate_response_for_review(user_follow_up, star_rating, streamlit.session_state["user_id"], THREAD_ID)
                        streamlit.session_state.chat_history.append({"user": user_follow_up, "assistant": response})
                        streamlit.rerun()