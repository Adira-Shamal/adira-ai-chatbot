import streamlit as st
import random

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

html, body, [class*="css"]{
    background-color:#0b1020;
    color:white;
    font-family:Arial;
}

.title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#a855f7;
    margin-top:20px;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:#cfcfcf;
    margin-bottom:30px;
}

.stTextInput input{
    background-color:#1e1e2f;
    color:white;
    border-radius:12px;
    border:2px solid #7c3aed;
    padding:14px;
    font-size:18px;
}

.stButton button{
    background:linear-gradient(90deg,#7c3aed,#a855f7);
    color:white;
    border:none;
    padding:14px;
    border-radius:12px;
    width:100%;
    font-size:18px;
    font-weight:bold;
}

.answer-box{
    background-color:#17172b;
    padding:25px;
    border-radius:18px;
    margin-top:25px;
    border:1px solid #7c3aed;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.markdown('<div class="title">🤖 AI Chatbot</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">Smart Educational Assistant</div>', unsafe_allow_html=True)

# =========================
# CHAT HISTORY
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# RESPONSE FUNCTION
# =========================

def chatbot_response(question):

    q = question.lower()

    responses = {

        "artificial intelligence":
        [
            "Artificial Intelligence (AI) enables machines to perform tasks that normally require human intelligence.",
            "AI is widely used in healthcare, robotics, automation, and virtual assistants.",
        ],

        "generative ai":
        [
            "Generative AI creates new content such as text, images, videos, and music.",
            "Examples of Generative AI include ChatGPT and AI image generators.",
        ],

        "prompt engineering":
        [
            "Prompt Engineering is the process of designing effective instructions for AI systems.",
            "It helps AI models generate more accurate and useful responses.",
        ],

        "machine learning":
        [
            "Machine Learning allows computers to learn patterns from data automatically.",
            "It is used in recommendation systems, fraud detection, and self-driving cars.",
        ],

        "python":
        [
            "Python is one of the most popular programming languages in the world.",
            "It is widely used in AI, web development, and data science.",
        ],

        "streamlit":
        [
            "Streamlit is a Python framework used for building web applications easily.",
            "It is very popular for AI and data science projects.",
        ],

        "chatgpt":
        [
            "ChatGPT is an AI chatbot developed by OpenAI.",
            "It can answer questions and generate human-like conversations.",
        ],

        "education":
        [
            "Education helps people gain knowledge and skills for personal development.",
            "Modern education also includes technology and AI-based learning systems.",
        ],

        "sports":
        [
            "Sports improve teamwork, discipline, and physical fitness.",
            "Popular sports include cricket, football, hockey, and tennis.",
        ],

        "quaid":
        [
            "Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan.",
            "He played a major role in the independence movement.",
        ],

        "iqbal":
        [
            "Allama Iqbal was a philosopher, poet, and thinker.",
            "His poetry inspired the idea of a separate Muslim state.",
        ]
    }

    for keyword in responses:

        if keyword in q:
            return random.choice(responses[keyword])

    return f"""
{question.title()} is an interesting topic.

Different experts explain this topic in different ways depending on context and application.

This chatbot currently provides educational and AI-related information.
"""

# =========================
# INPUT
# =========================

question = st.text_input("Ask your question")

# =========================
# BUTTON
# =========================

if st.button("Generate Response"):

    if question:

        answer = chatbot_response(question)

        st.session_state.messages.append(
            ("You", question)
        )

        st.session_state.messages.append(
            ("AI", answer)
        )

# =========================
# DISPLAY CHAT
# =========================

for sender, message in st.session_state.messages:

    if sender == "You":

        st.markdown(f"""
        <div class="answer-box">
        <b>🧑 You:</b><br><br>
        {message}
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="answer-box">
        <b>🤖 AI:</b><br><br>
        {message}
        </div>
        """, unsafe_allow_html=True)
