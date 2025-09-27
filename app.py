import streamlit as st
from langchain_groq import ChatGroq  # Changed from ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
import openai # Removed, as Groq integration doesn't need the generic openai library

# Load environment variables (for LangSmith tracing)
load_dotenv()

## Langsmith Tracking (Assuming you have these keys set locally or in Streamlit Secrets)
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With GROQ" # Updated project name

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond concisely to the user queries."),
        ("user", "Question:{question}")
    ]
)

def generate_response(question, api_key, engine, temperature, max_tokens):
    """
    Generates a response using the ChatGroq model with the provided parameters.
    """
    
    # Initialize ChatGroq, passing the API key, model name, and parameters
    llm = ChatGroq(
        model=engine,
        groq_api_key=api_key, # Use the key passed from the sidebar
        temperature=temperature,
        max_tokens=max_tokens,
        streaming=True # Enable streaming for better UX
    )
    
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    
    # We use st.write_stream to render the response chunks immediately
    response = st.write_stream(chain.stream({'question': question}))
    
    # The final streamed content is returned by st.write_stream
    return response

## Title of the app
st.title("⚡ Groq-Powered Q&A Chatbot")
st.markdown("---")

# Sidebar for settings
st.sidebar.title("Settings")

# --- UI Changes for Groq ---
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Select the Groq model
engine = st.sidebar.selectbox(
    "Select Groq Model",
    [
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
        "llama3-8b-8192"
    ],
    index=1 # Defaulting to Gemma2-9b-It for good performance/speed balance
)
# --- End UI Changes ---

## Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main interface for user input
st.write("Go ahead and ask any question.")
user_input = st.text_input("You:")

if user_input and api_key:
    # Use a chat message container for the response for better visual style
    with st.chat_message("assistant"):
        # The generate_response function now streams the response directly to the UI
        generate_response(user_input, api_key, engine, temperature, max_tokens)
    
elif user_input:
    st.warning("Please enter the Groq API Key in the side bar.")
else:
    # Changed the default message slightly
    st.info("Start the conversation above to see the results.")