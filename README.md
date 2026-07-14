# 🤖 LangGraph Streamlit Chatbot with Groq LLM

A conversational AI chatbot built using **LangGraph**, **LangChain**, **Groq LLM**, and **Streamlit**.
The application demonstrates stateful conversations using LangGraph memory and provides a simple web-based chat interface.

## 🚀 Features

* Chat with an AI assistant using Groq LLM
* Built with LangGraph StateGraph workflow
* Conversation memory using LangGraph Checkpoint
* Streamlit chat interface
* Environment variable support for API keys
* Clean chatbot architecture using nodes and states

## 🏗️ Architecture

```
User
 |
 v
Streamlit Chat UI
 |
 v
LangGraph StateGraph
 |
 |---- ChatState
 |
 |---- Chatbot Node
 |
 v
Groq LLM
 |
 v
AI Response
 |
 v
Memory Checkpoint
```

## 🛠️ Tech Stack

* Python
* Streamlit
* LangGraph
* LangChain
* Groq API
* Pydantic
* python-dotenv

## 📂 Project Structure

```
langgraph-streamlit-chatbot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not committed)
├── .env.example           # Example environment variables
├── .gitignore             # Git ignored files
└── README.md              # Project documentation
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langgraph-streamlit-chatbot.git

cd langgraph-streamlit-chatbot
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Setup

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

```
https://console.groq.com/
```

## ▶️ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

## 🧠 How Memory Works

The chatbot uses LangGraph checkpoint memory:

```
Thread ID
    |
    v
Conversation State
    |
    v
Message History
    |
    v
AI Response
```

Each conversation is maintained using a unique:

```python
thread_id
```

## 💡 Future Improvements

* Add PostgreSQL persistent chat memory
* Add user authentication
* Add RAG document search
* Add web search tools
* Add chat history database
* Deploy using Docker and AWS

## 📌 Learning Goals

This project demonstrates:

* Building AI agents with LangGraph
* Managing LLM workflows
* Stateful chatbot development
* Integrating LLM APIs into web applications
* Creating production-style AI applications

## 👨‍💻 Author

Your Name

GitHub:

```
https://github.com/your-username
```
