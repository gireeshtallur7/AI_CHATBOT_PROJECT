import streamlit as st
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

st.write("API Key Found:", "MISTRAL_API_KEY" in st.secrets)

llm_model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.7
)

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.markdown(
    """
    <style>
    .main {
        padding-top: 2rem;
    }
    .stChatMessage {
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 AI Assistant")

mode_choice = st.selectbox(
    "Choose your system message",
    (
        "😡 Angry Mode",
        "😢 Sad Mode",
        "😊 Normal Mode"
    )
)

if mode_choice == "😡 Angry Mode":
    mode = "you are an angry ai assistant so that you always respond in angry tone"
elif mode_choice == "😢 Sad Mode":
    mode = "you are a sad ai assistant so that you always respond in sad tone"
else:
    mode = "you are a normal ai assistant so that you always respond in normal tone"

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]

if st.session_state.messages[0].content != mode:
    st.session_state.messages = [SystemMessage(content=mode)]

for msg in st.session_state.messages[1:]:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    response = llm_model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.markdown(response.content)