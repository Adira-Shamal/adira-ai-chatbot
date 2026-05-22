import streamlit as st

# ====================================
# PAGE SETTINGS
# ====================================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ====================================
# CUSTOM CSS
# ====================================

st.markdown("""
<style>

#MainMenu {
    visibility:hidden;
}

footer {
    visibility:hidden;
}

header {
    visibility:hidden;
}

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

</style>
""", unsafe_allow_html=True)

# ====================================
# TITLE
# ====================================

st.markdown(
    '<div class="title">🤖 AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Educational Assistant</div>',
    unsafe_allow_html=True
)

# ====================================
# RESPONSE FUNCTION
# ====================================

def chatbot_response(question):

    q = question.lower()

    responses = {

        "artificial intelligence":
        """
Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that normally require human intelligence.

These tasks include learning, reasoning, decision-making, and language understanding. AI is widely used in healthcare, robotics, automation, and virtual assistants.
""",

        "generative ai":
        """
Generative AI is a type of Artificial Intelligence that can create new content such as text, images, videos, music, and code.

Popular examples include ChatGPT and AI image generators. It is widely used in education, media, and software development.
""",

        "prompt engineering":
        """
Prompt Engineering is the process of writing effective instructions or questions for AI systems to generate better responses.

It is considered an important skill because good prompts improve the quality and accuracy of AI-generated outputs.
""",

        "machine learning":
        """
Machine Learning is a branch of AI that allows computers to learn automatically from data without being explicitly programmed.

It is used in recommendation systems, fraud detection, image recognition, and many modern technologies.
""",

        "python":
        """
Python is one of the most popular programming languages in the world.

It is known for its simple syntax and is widely used in Artificial Intelligence, web development, automation, and data science.
""",

        "streamlit":
        """
Streamlit is a Python framework used to create web applications quickly and easily.

It is especially popular in AI and data science projects because developers can build interactive applications with minimal code.
""",

        "chatgpt":
        """
ChatGPT is an AI chatbot developed by OpenAI.

It can understand questions and generate human-like responses. It is widely used for education, coding help, research, and content generation.
""",

        "education":
        """
Education is the process of gaining knowledge, skills, values, and understanding.

It plays an important role in personal growth and social development. Modern education also includes technology, online learning, and AI-based systems.
""",

        "sports":
        """
Sports are physical activities that improve fitness, teamwork, discipline, and mental strength.

Popular sports include cricket, football, hockey, basketball, and tennis.
""",

        "quaid":
        """
Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan.

He played a major role in the independence movement and worked for the rights of Muslims in the subcontinent.
""",

        "iqbal":
        """
Allama Muhammad Iqbal was a famous philosopher, poet, and thinker.

His poetry inspired Muslims and promoted the idea of a separate Muslim state.
""",

        "physics":
        """
Physics is the branch of science that studies matter, energy, force, motion, and the laws of the universe.

It explains how objects move and interact with each other and is important in engineering and technology.
""",

        "chemistry":
        """
Chemistry is the study of substances, elements, compounds, and chemical reactions.

It helps us understand how materials interact and change in daily life and industry.
""",

        "biology":
        """
Biology is the branch of science that studies living organisms and life processes.

It includes topics such as plants, animals, genetics, microorganisms, and the human body.
"""
    }

    for keyword in responses:

        if keyword in q:
            return responses[keyword]

    return f"""
{question.title()} is an important and interesting topic.

Different experts explain this topic in different ways depending on context and application.

This chatbot currently provides educational and AI-related information for selected topics.
"""

# ====================================
# INPUT
# ====================================

question = st.text_input("Ask your question")

# ====================================
# BUTTON
# ====================================

if st.button("Generate Response"):

    if question:

        answer = chatbot_response(question)

        # OLD ANSWER REMOVE HOGA
        st.session_state.current_question = question
        st.session_state.current_answer = answer

# ====================================
# DISPLAY CURRENT CHAT ONLY
# ====================================

if "current_question" in st.session_state:

    st.write("### 🧑 You")
    st.info(st.session_state.current_question)

    st.write("### 🤖 AI")
    st.success(st.session_state.current_answer)
