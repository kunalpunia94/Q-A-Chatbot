# 🚀 Groq-Powered Q&A Chatbot (Streamlit & LangChain)

This project demonstrates a simple yet extremely fast Question & Answer chatbot built using **Streamlit** for the frontend UI and the **Groq API via LangChain** for real-time inference.

The app is built to showcase high-speed, configurable LLM interaction.

[Live Demo](https://chatbotmultimodal.streamlit.app/) | [GitHub Repo](https://github.com/kunalpunia94/Q-A-Chatbot)

---

## ✨ Key Features

- **Inference Engine:** Uses the Groq LPU™ Inference Engine for exceptionally fast, low-latency responses.
- **Technology Stack:** Leverages LangChain Expression Language (LCEL) to create a clean pipeline (Prompt | LLM | Parser).
- **Configurable Settings:** Allows users to dynamically select the Groq model (e.g., `llama-3.1-8b-instant`), adjust response Temperature, and set Max Tokens via the Streamlit sidebar.
- **Security:** Prompts for the Groq API key in the sidebar for secure, session-based access.

---

## ⚙️ Requirements

### 1. API Key
You require an API key from Groq to run the language model.

- **API Key Required:** `GROQ_API_KEY`
- **Source:** Obtain your key from the [Groq Console](https://console.groq.com/).

### 2. Dependencies
All required Python packages must be installed. The project dependencies are listed in `requirements.txt`.

### 3. LLM Models Used
The application utilizes high-performance models available on the Groq platform, including:

- `llama-3.1-8b-instant`
- `gemma2-9b-it`
- `llama-3.3-70b-versatile`

---

## 🛠️ Setup and Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/kunalpunia94/Q-A-Chatbot
cd Q-A-Chatbot
