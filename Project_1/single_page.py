import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os

orders=[
  {
    "order_id": "ORD-2001",
    "customer": "Ananya",
    "product_id": "P201",
    "product_name": "Smart Watch",
    "status": "Shipped",
    "estimated_delivery": "2026-09-09",
    "price": 5999
  },
  {
    "order_id": "ORD-2002",
    "customer": "Vikram",
    "product_id": "P202",
    "product_name": "Wireless Earbuds",
    "status": "Processing",
    "estimated_delivery": "2026-09-11",
    "price": 2999
  },
  {
    "order_id": "ORD-2003",
    "customer": "Sneha",
    "product_id": "P203",
    "product_name": "Laptop Stand",
    "status": "Delivered",
    "estimated_delivery": "2026-09-05",
    "price": 1799
}


 ]
st.title("AI CUSTOMER SUPPORT AGENT")
user_query=st.text_input("Enter your query:")

client = OpenAI()

response = client.responses.create(
    model="gpt-6-astra",
    input=[
        {
            "role": "system",
            "content": f"You are a customer support agent for an e-commerce platform. You will be provided with a user's query and a list of order details. Your task is to provide a helpful and accurate response to the user's query based on the {orders} details. Nothing else should be included in your response. If the user's query is not related to the order details, politely inform them that you can only assist with order-related queries."
        },
        {
            "role": "user",
            "content": user_query
        }
    ]
)

st.write(response.output_text)