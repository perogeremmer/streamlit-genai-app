import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="Chatbot Kenari", page_icon=":")
st.title("Chatbot Kenari")

api_key = os.getenv("KENARI_API_KEY")
if not api_key:
    st.warning("KENARI_API_KEY belum diisi di file .env")
    st.stop()

client = OpenAI(base_url="https://kenari.id/v1", api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    model = st.text_input("Model", value="deepseek-v4-1-flash")
    if st.button("Clear Chat"):
        st.session_state.messages = []
    st.caption("Gateway: kenari.id/v1")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Tulis pesan..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Kenari sedang berpikir..."):
            r = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages,
            )
        answer = r.choices[0].message.content
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
