# 🤖 AI Customer Support Agent : Project for Module-3

An AI-powered customer support assistant built with **Python, OpenAI, and Streamlit**. It answers customer queries using tools and mock JSON data instead of guessing.

## 🎯 Problem

Small online businesses receive repetitive customer-support questions such as:

* Where is my order?
* Can I return my product?
* Is my order eligible for a refund?
* Why hasn't my order arrived?
* Can I cancel my order?

A basic chatbot may guess incorrectly because it does not have access to actual order information.

This project solves the problem using **AI, tool calling, mock order data, and predefined store policies**.

## 🎯 Objective

The agent can:

* Understand customer questions
* Identify when order information is required
* Retrieve order information from a mock database
* Search product details
* Apply predefined store policies
* Use OpenAI tool calling
* Maintain conversation context
* Prevent hallucinated information
* Return customer-friendly responses
* Return structured actions for other systems

## 🛠️ Tech Stack

* Python
* OpenAI API
* Streamlit
* Pydantic
* python-dotenv
* JSON

## 📁 Project Structure

```text
AI_Customer_Support_Agent/
├── app.py
├── assistant.py
├── tools.py
├── schemas.py
├── prompts.py
├── requirements.txt
├── .env
├── README.md
└── data/
    ├── orders.json
    ├── products.json
    └── policies.json
```

## 🔧 Tools

| Tool              | Purpose                  |
| ----------------- | ------------------------ |
| `get_order`       | Retrieve order status    |
| `get_product`     | Retrieve product details |
| `search_products` | Search products          |
| `get_policy`      | Retrieve store policies  |

## 🚀 Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

## 💬 Example Queries

```text
Where is my order ORD-1001?
Tell me about product P102.
Show me computer accessories.
What is your return policy?
How long does a refund take?
```

## 🏗️ Architecture

```text
Customer
   ↓
Streamlit UI
   ↓
OpenAI LLM
   ↓
Tool Calling
   ↓
JSON Mock Database
   ↓
Tool Result
   ↓
Customer Response
   ↓
Structured Action
```

## 📌 Key Concepts

**LLM • Prompt Engineering • Tool Calling • Function Routing • JSON Data • Pydantic • Conversation Memory • Hallucination Control • Structured Actions**

## 📄 License

This project is created for **educational purposes – Module 3: Generative AI / LLM Application Development**.
