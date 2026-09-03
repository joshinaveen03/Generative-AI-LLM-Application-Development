# 🚀 Streamlit Basic LLM App

A beginner-to-intermediate project for learning Streamlit and LLM
application development.

This project progresses from basic Streamlit components to OpenAI,
Ollama, session state, caching, secrets, and AI chatbots.

📂 Project Structure

streamlit_Basic_LLM_APP/
│
├── .streamlit/
│   └── secrets.toml
│
├── 01_app.py
├── 02_slider.py
├── 03_counter.py
├── 04_counter_session_state.py
├── 05_widget_tour.py
├── 06_report.py
├── 07_progress_demo.py
├── 08_input_widgets.py
├── 09_llm_dashboard.py
├── 10_openai_llm_dashboard.py
├── 11_cache_demo.py
├── 12_secrets_demo.py
├── 13_ask_openai.py
├── 14_user_details.py
├── 15_ollama_chatbot.py
├── 16_ai_chatbot.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env

🧠 Learning Modules

File                            Concept

01_app.py                     First Streamlit App
02_slider.py                  Slider
03_counter.py                 Button & Variables
04_counter_session_state.py   Session State
05_widget_tour.py             Streamlit Widgets
06_report.py                  Tables, Metrics & Messages
07_progress_demo.py           Spinner & Progress
08_input_widgets.py           Input Widgets
09_llm_dashboard.py           Dashboard Layout
10_openai_llm_dashboard.py    OpenAI Dashboard
11_cache_demo.py              Caching
12_secrets_demo.py            Secure Secrets
13_ask_openai.py              OpenAI API
14_user_details.py            User Input
15_ollama_chatbot.py          Ollama Chatbot
16_ai_chatbot.py              Complete AI Chatbot

🛠️ Technologies

Python

Streamlit

OpenAI API

Ollama

Qwen

Pandas

Python-dotenv

⚙️ Setup

1. Create virtual environment

python -m venv venv

2. Activate environment --- Windows

venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

▶️ Run Streamlit

Example:

streamlit run 01_app.py

Run the complete AI chatbot:

streamlit run 16_ai_chatbot.py

Stop Streamlit:

Ctrl + C

🔐 OpenAI Secrets

Create:

.streamlit/
└── secrets.toml

Add:

OPENAI_API_KEY = "your-openai-api-key"

Use in Python:

import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]

Never commit API keys or secrets.toml to GitHub.

🦙 Ollama

Install:

pip install ollama

Download the model:

ollama pull qwen3:1.7b

Run:

streamlit run 15_ollama_chatbot.py

🤖 AI Chatbot Flow

User
  ↓
Streamlit Chat UI
  ↓
Chat Input
  ↓
Session State
  ↓
OpenAI / Ollama
  ↓
LLM Response
  ↓
Chat History
  ↓
Streamlit UI

📚 Learning Path

Python
   ↓
Streamlit Basics
   ↓
Widgets
   ↓
Layouts
   ↓
Session State
   ↓
Caching
   ↓
Secrets
   ↓
OpenAI API
   ↓
Ollama
   ↓
AI Chatbot
   ↓
LangChain
   ↓
LangGraph

🎯 Next Steps

Streaming LLM responses

LangChain integration

LangGraph workflows

RAG application

Document Q&A

Vector database

Production deployment

👨‍💻 Author

Naveen Joshi

Learning and building AI applications with:

Python • Streamlit • OpenAI • Ollama • LangChain • LangGraph