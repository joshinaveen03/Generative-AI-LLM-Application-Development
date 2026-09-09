from typing import Optional
from pydantic import BaseModel


class OrderResponse(BaseModel):
    order_id: str
    product_name: str
    status: str
    estimated_delivery: str
    price: float


class ProductResponse(BaseModel):
    product_id: str
    name: str
    category: str
    price: float
    stock: int
    description: str


class PolicyResponse(BaseModel):
    policy_name: str
    description: str


class AssistantResponse(BaseModel):
    answer: str
    source: Optional[str] = None
    tool_used: Optional[str] = None

