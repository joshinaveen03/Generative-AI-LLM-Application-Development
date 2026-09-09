import json
from dotenv import load_dotenv
from openai import OpenAI

from prompts import SYSTEM_PROMPT
from tools import call_tool

load_dotenv()

client = OpenAI()

TOOLS = [
    {
        "type": "function",
        "name": "get_order",
        "description": "Get the current details and status of an order.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Order ID such as ORD-1001"
                }
            },
            "required": ["order_id"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "get_product",
        "description": "Get details about a specific product.",
        "parameters": {
            "type": "object",
            "properties": {
                "product_id": {
                    "type": "string",
                    "description": "Product ID such as P101"
                }
            },
            "required": ["product_id"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "search_products",
        "description": "Search products by name, category or description.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Product search query"
                }
            },
            "required": ["query"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "get_policy",
        "description": "Retrieve return, refund, shipping or warranty policy.",
        "parameters": {
            "type": "object",
            "properties": {
                "policy_name": {
                    "type": "string",
                    "description": "Policy such as return, refund, shipping or warranty"
                }
            },
            "required": ["policy_name"],
            "additionalProperties": False
        }
    }
]


def run_assistant(user_message, conversation_history):
    input_messages = []

    for message in conversation_history:
        input_messages.append({
            "role": message["role"],
            "content": message["content"]
        })

    input_messages.append({
        "role": "user",
        "content": user_message
    })

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=SYSTEM_PROMPT,
        input=input_messages,
        tools=TOOLS
    )

    input_messages += response.output
    tool_was_called = False

    for item in response.output:
        if item.type != "function_call":
            continue

        tool_was_called = True
        arguments = json.loads(item.arguments)

        result = call_tool(item.name, arguments)

        input_messages.append({
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": json.dumps(result)
        })

    if tool_was_called:
        final_response = client.responses.create(
            model="gpt-4o-mini",
            instructions=SYSTEM_PROMPT,
            input=input_messages,
            tools=TOOLS
        )
        return final_response.output_text

    return response.output_text

