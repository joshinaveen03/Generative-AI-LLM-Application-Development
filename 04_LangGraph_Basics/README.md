README.md
# LangGraph Learning

A beginner-friendly collection of **LangGraph** examples for learning State, Nodes, Edges, workflows, chatbot memory, and OpenAI LLM integration.

## 📂 Project Structure

```text
Langraphs/
│
├── 01_basic_langgraph.py
├── 02_langgraph_state_update.py
├── 03_langgraph_sequential_nodes.py
├── 04_langgraph_multiple_nodes.py
├── 05_langgraph_basic_state_graph.py
├── 06_langgraph_state_processing.py
├── 07_langgraph_chatbot_memory.py
├── 08_basic_langgraph_greeting.py
├── 09_langgraph_Three_question_answer.py
├── 10_basic_langgraph_openai.py
├── 11_basic_langgraph_openai.py
├── 12_langgraph_three_question_with_partial_answer.py
├── 13_langgraph_generate_improve_answer.py
│
├── README.md
└── .env
🧠 LangGraph

LangGraph is used to build stateful workflows and AI applications using:

State – Stores application data
Nodes – Perform tasks
Edges – Define workflow
START / END – Workflow boundaries
LLMs – Generate and process responses
Basic Flow
START
  ↓
Node 1
  ↓
Node 2
  ↓
END
🛠️ Installation
pip install langgraph langchain langchain-openai python-dotenv

Create .env:

OPENAI_API_KEY=your_api_key

Add .env to .gitignore.

🎯 Learning Path
Basic Graph
   ↓
State
   ↓
Multiple Nodes
   ↓
Sequential Workflow
   ↓
Chatbot Memory
   ↓
OpenAI Integration
   ↓
LLM Workflows
🚀 Goal

Learn LangGraph step-by-step and build LLM-powered workflows and AI agents with Python.