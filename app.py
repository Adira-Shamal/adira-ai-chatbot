import streamlit as st
from openai import OpenAI

# =========================
# OPENROUTER API
# =========================

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="PASTE_YOUR_OPENROUTER_API_KEY"
)

# =========================
# PAGE
# =========================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")

question = st.text_input("Ask anything")

# =========================
# BUTTON
# =========================

if st.button("Generate Response"):

    if question:

        try:

            completion = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = completion.choices[0].message.content

            st.markdown("## Answer")

            st.write(answer)

        except Exception as e:

            st.error(e)

    else:

        st.warning("Please enter a question.")