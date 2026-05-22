import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# =========================
# LOAD ENV
# =========================

load_dotenv()

# =========================
# GROQ API
# =========================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# =========================
# TITLE
# =========================

st.title("🤖 AI Chatbot")

st.write("Ask anything")

# =========================
# INPUT
# =========================

question = st.text_input("Enter your question")

# =========================
# BUTTON
# =========================

if st.button("Generate Response"):

    if question:

        try:

            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = response.choices[0].message.content

            st.markdown("## Answer")

            st.write(answer)

        except Exception as e:

            st.error(e)

    else:

        st.warning("Please enter a question.")
