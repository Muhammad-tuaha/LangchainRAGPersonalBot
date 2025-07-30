import streamlit as st
import requests

st.title("🤖 RAG Chatbot")

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
query = st.text_input("Ask me something:", key="input")

# Submit button
if st.button("Send") and query:
    # Call FastAPI backend
    try:
        response = requests.get("http://127.0.0.1:8000/", params={"query": query})
        result = response.json().get("response", "No response")

        # Append to history
        st.session_state.chat_history.append(("You", query))
        st.session_state.chat_history.append(("Bot", result))

    except Exception as e:
        st.error(f"Error: {e}")

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
