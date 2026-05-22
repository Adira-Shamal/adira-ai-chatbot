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
    font-size:18px;
    line-height:1.7;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.markdown(
    '<div class="title">🤖 AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Educational Assistant</div>',
    unsafe_allow_html=True
)

# =========================
# RESPONSE FUNCTION
# =========================

def chatbot_response(question):

    q = question.lower()

    responses = {

        "artificial intelligence":
        [
            """
Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that normally require human intelligence. These tasks include learning, problem solving, decision making, and understanding language.

AI is widely used in modern technology such as virtual assistants, self-driving cars, recommendation systems, healthcare, and robotics. It helps improve efficiency and automation in different industries.
"""
        ],

        "generative ai":
        [
            """
Generative AI is a type of Artificial Intelligence that can create new content such as text, images, videos, music, and code.

Popular examples include ChatGPT and AI image generators. Generative AI is becoming very important in education, software development, media, and business industries.
"""
        ],

        "prompt engineering":
        [
            """
Prompt Engineering is the process of writing effective instructions or questions for AI systems in order to get better responses.

It is considered an important skill in modern AI applications because the quality of prompts directly affects the quality of AI-generated output.
"""
        ],

        "machine learning":
        [
            """
Machine Learning is a branch of Artificial Intelligence that allows computers to learn automatically from data without being explicitly programmed.

Machine Learning is used in recommendation systems, fraud detection, image recognition, and many modern AI applications.
"""
        ],

        "python":
        [
            """
Python is one of the most popular programming languages in the world. It is known for its simple syntax and beginner-friendly structure.

Python is widely used in Artificial Intelligence, web development, automation, cybersecurity, and data science projects.
"""
        ],

        "streamlit":
        [
            """
Streamlit is a Python framework used for building web applications quickly and easily.

It is especially popular in AI and data science projects because developers can create interactive applications with very little code.
"""
        ],

        "chatgpt":
        [
            """
ChatGPT is an AI chatbot developed by OpenAI. It is capable of understanding user questions and generating human-like responses.

It is used for education, coding help, writing assistance, research, and many other purposes.
"""
        ],

        "education":
        [
            """
Education is the process of gaining knowledge, skills, values, and understanding. It plays an important role in personal growth and social development.

Modern education also includes technology, online learning, and AI-based educational systems.
"""
        ],

        "sports":
        [
            """
Sports are physical activities that improve fitness, teamwork, discipline, and mental strength.

Popular sports around the world include cricket, football, hockey, basketball, and tennis. Sports also play an important role in entertainment and international competitions.
"""
        ],

        "quaid":
        [
            """
Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan and an important political leader.

He played a major role in the independence movement and worked for the rights of Muslims in the subcontinent. Pakistan achieved independence in 1947 under his leadership.
"""
        ],

        "iqbal":
        [
            """
Allama Muhammad Iqbal was a famous philosopher, poet, and thinker. His poetry inspired Muslims and promoted the idea of a separate Muslim state.

He is also known as the spiritual father of Pakistan because of his vision and ideas.
"""
        ],

        "physics":
        [
            """
Physics is the branch of science that studies matter, energy, force, motion, and the laws of the universe.

It explains how objects move and interact with each other. Physics is important in engineering, technology, space science, and many other scientific fields.
"""
        ],

        "chemistry":
        [
            """
Chemistry is the study of substances, elements, compounds, and chemical reactions.

It helps us understand how materials interact and change. Chemistry is widely used in medicine, industry, agriculture, and environmental science.
"""
        ],

        "biology":
        [
            """
Biology is the branch of science that studies living organisms and life processes.

It includes topics such as plants, animals, genetics, human body systems, and microorganisms. Biology is important in medicine and healthcare fields.
"""
        ]
    }

    for keyword in responses:

        if keyword in q:
            return random.choice(responses[keyword])

    return f"""
{question.title()} is an important and interesting topic.

Different experts explain this topic in different ways depending on context and application. This chatbot currently provides educational and AI-related information for selected topics.
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

        # OLD ANSWER REMOVE HOGA
        st.session_state.current_question = question
        st.session_state.current_answer = answer

# =========================
# DISPLAY CURRENT CHAT ONLY
# =========================

if "current_question" in st.session_state:

    st.markdown(f"""
    <div class="answer-box">
    <b>🧑 You:</b><br><br>
    {st.session_state.current_question}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="answer-box">
    <b>🤖 AI:</b><br><br>
    {st.session_state.current_answer}
    </div>
    """, unsafe_allow_html=True)
