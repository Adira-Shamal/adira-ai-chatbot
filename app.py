import streamlit as st

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
    background-color:#070b17;
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
    color:#cccccc;
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

st.markdown('<div class="subtitle">Ask Anything</div>', unsafe_allow_html=True)

# =========================
# INPUT
# =========================

question = st.text_input("Enter your question")

# =========================
# ANSWER FUNCTION
# =========================

def generate_answer(q):

    q = q.lower()

    if "artificial intelligence" in q or q == "ai":

        return """
Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that usually require human intelligence.

AI systems can learn from data, recognize speech, solve problems, and make decisions.

Examples of AI include chatbots, self-driving cars, recommendation systems, and virtual assistants.
"""

    elif "generative ai" in q:

        return """
Generative AI is a type of Artificial Intelligence that creates new content such as text, images, music, videos, and code.

Examples include ChatGPT and AI image generators.

It is widely used in education, media, and software development.
"""

    elif "prompt engineering" in q:

        return """
Prompt Engineering is the process of writing effective instructions for AI systems.

It helps AI generate better and more accurate responses.

This skill is important in modern AI applications.
"""

    elif "machine learning" in q:

        return """
Machine Learning is a branch of AI that allows computers to learn automatically from data.

It is used in recommendation systems, spam filters, and self-driving cars.
"""

    elif "python" in q:

        return """
Python is a popular programming language known for its simple syntax.

It is widely used in AI, web development, automation, and data science.
"""

    elif "streamlit" in q:

        return """
Streamlit is a Python framework used to create web applications quickly and easily.

It is popular for AI and data science projects.
"""

    elif "chatgpt" in q:

        return """
ChatGPT is an AI chatbot developed by OpenAI.

It can understand questions and generate human-like responses.
"""

    elif "education" in q:

        return """
Education is the process of gaining knowledge, skills, and values.

It plays an important role in personal and social development.
"""

    elif "sports" in q:

        return """
Sports improve physical health, teamwork, and discipline.

Popular sports include cricket, football, hockey, and tennis.
"""

    elif "quaid" in q or "jinnah" in q:

        return """
Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan.

He played a major role in the independence of Pakistan in 1947.
"""

    elif "iqbal" in q:

        return """
Allama Muhammad Iqbal was a philosopher and poet.

He inspired Muslims through his poetry and ideas.
"""

    else:

        return f"""
{q.title()} is an important topic.

Different experts explain this topic in different ways depending on the situation and context.

This AI chatbot provides general educational information about selected topics.
"""

# =========================
# BUTTON
# =========================

if st.button("Generate Response"):

    if question.strip() != "":

        answer = generate_answer(question)

        st.markdown("## Answer")

        st.write(answer)

    else:

        st.warning("Please enter a question.")
