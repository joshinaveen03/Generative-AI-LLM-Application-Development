import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


def get_order(order_id: str):
    for order in load_json("orders.json"):
        if order["order_id"].lower() == order_id.lower():
            return order
    return {"error": f"Order {order_id} was not found."}


def get_product(product_id: str):
    for product in load_json("products.json"):
        if product["product_id"].lower() == product_id.lower():
            return product
    return {"error": f"Product {product_id} was not found."}


def search_products(query: str):
    products = load_json("products.json")
    query = query.lower()
    results = []

    for product in products:
        text = (
            product["name"] + " " +
            product["category"] + " " +
            product["description"]
        ).lower()

        if query in text:
            results.append(product)

    return {"results": results} if results else {
        "message": "No matching products found.",
        "results": []
    }


def get_policy(policy_name: str):
    policies = load_json("policies.json")
    aliases = {
        "return": "return_policy",
        "returns": "return_policy",
        "refund": "refund_policy",
        "shipping": "shipping_policy",
        "delivery": "shipping_policy",
        "warranty": "warranty_policy"
    }

    key = aliases.get(policy_name.lower(), policy_name.lower())

    if key not in policies:
        return {"error": f"Policy '{policy_name}' was not found."}

    return {"policy_name": key, **policies[key]}


def call_tool(name, arguments):
    if name == "get_order":
        return get_order(**arguments)
    if name == "get_product":
        return get_product(**arguments)
    if name == "search_products":
        return search_products(**arguments)
    if name == "get_policy":
        return get_policy(**arguments)

    return {"error": f"Unknown tool: {name}"}
