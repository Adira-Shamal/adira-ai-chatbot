import streamlit as st

st.set_page_config(page_title="Adira AI Chatbot", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0d1117;
}

.main {
    background-color: #0d1117;
}

.title {
    text-align: center;
    font-size: 45px;
    color: white;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #c9d1d9;
    margin-bottom: 30px;
}

.stTextInput > div > div > input {
    background-color: #161b22;
    color: white;
    border-radius: 10px;
    border: 1px solid #30363d;
}

.answer-box {
    background-color: #161b22;
    padding: 20px;
    border-radius: 15px;
    color: white;
    margin-top: 20px;
    border: 1px solid #30363d;
}

</style>
""", unsafe_allow_html=True)


st.markdown("<div class='title'>🤖 Adira AI Chatbot</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Educational Rule-Based AI Chatbot</div>", unsafe_allow_html=True)

question = st.text_input("Ask your question:")


def get_answer(question):

    question = question.lower()

    responses = {

        "what is python":
        "Python is a powerful and beginner-friendly programming language used in AI, web development, automation, and software development.",

        "what is ai":
        "Artificial Intelligence (AI) is a technology that allows machines to simulate human intelligence and perform smart tasks.",

        "what is artificial intelligence":
        "Artificial Intelligence is the field of computer science focused on building intelligent systems and smart machines.",

        "what is generative ai":
        "Generative AI is a type of AI that can generate text, images, code, and other content automatically.",

        "what is machine learning":
        "Machine Learning is a branch of AI that allows computers to learn from data and improve automatically.",

        "what is prompt engineering":
        "Prompt Engineering is the process of creating effective instructions for AI models to generate accurate responses.",

        "what is streamlit":
        "Streamlit is a Python framework used to build interactive web applications and AI dashboards.",

        "what is chatbot":
        "A chatbot is a software application that communicates with users and provides automated responses.",

        "what is education":
        "Education is the process of gaining knowledge, skills, values, and understanding for personal and social development.",

        "what is physics":
        "Physics is the branch of science that studies matter, energy, motion, force, and the laws of nature.",

        "what is chemistry":
        "Chemistry is the branch of science that studies substances, chemical reactions, and matter.",

        "what is biology":
        "Biology is the scientific study of living organisms including humans, animals, and plants.",

        "who is quaid e azam":
        "Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan and the first Governor-General of Pakistan.",

        "who is allama iqbal":
        "Allama Muhammad Iqbal was a famous philosopher, poet, and thinker who inspired the idea of Pakistan.",

        "what is computer":
        "A computer is an electronic machine that processes data and performs tasks according to instructions.",

        "what is internet":
        "The internet is a global network that connects computers and allows communication and information sharing worldwide."
    }

    for key in responses:
        if key in question:
            return responses[key]

    return "Sorry, I can only answer educational and AI-related questions in this chatbot demo."


if st.button("Generate Response"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:
        answer = get_answer(question)

        st.markdown(f"""
        <div class="answer-box">
        <h3>🤖 AI Response</h3>
        <p>{answer}</p>
        </div>
        """, unsafe_allow_html=True)
