import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Import for Speech Recognition
import speech_recognition as sr

# Load environment variables from .env file
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked"),
        ("user", "Question:{question}")
    ]
)

## Streamlit framework
st.title("Langchain Demo With Gemma Model")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Function to handle speech recognition
def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Say something!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio) # Using Google Web Speech API for simplicity
            st.session_state.audio_input = text # Store transcribed text in session state
            st.success(f"You said: {text}")
        except sr.UnknownValueError:
            st.error("Could not understand audio")
            st.session_state.audio_input = ""
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
            st.session_state.audio_input = ""

# Add a button for speech input
st.button("🎤 Speak Your Question", on_click=transcribe_speech)

# Check if there's transcribed audio and use it as input
if "audio_input" in st.session_state and st.session_state.audio_input:
    user_query = st.session_state.audio_input
    # Clear the audio input so it doesn't trigger repeatedly on reruns
    st.session_state.audio_input = ""
else:
    user_query = None # No speech input yet, or it was cleared

# Accept user text input (still available)
text_input = st.chat_input("Type your question here...")
if text_input:
    user_query = text_input

# Process user query (either from speech or text)
if user_query:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_query})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_query)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = chain.invoke({"question": user_query})
            st.markdown(ai_response)
    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})


