import streamlit as st
from langchain_groq import ChatGroq  # Changed from ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With GROQ" # 

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
        groq_api_key=api_key, 
        temperature=temperature,
        max_tokens=max_tokens,
        streaming=True 
    )
    
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    
    response = st.write_stream(chain.stream({'question': question}))
    
    return response

st.title("⚡ Groq-Powered Q&A Chatbot")
st.markdown("---")

st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

engine = st.sidebar.selectbox(
    "Select Groq Model",
    [
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
        "llama3-8b-8192"
    ],
    index=1 
)

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("Go ahead and ask any question.")
user_input = st.text_input("You:")

if user_input and api_key:
    with st.chat_message("assistant"):
        generate_response(user_input, api_key, engine, temperature, max_tokens)
    
elif user_input:
    st.warning("Please enter the Groq API Key in the side bar.")
else:
    st.info("Start the conversation above to see the results.")
