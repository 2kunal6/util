import requests
import streamlit as st
import subprocess


st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})



# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = requests.get(f'http://faiss:8000/predict?prompt={prompt}')
    st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
