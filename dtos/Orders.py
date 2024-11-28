from typing import Optional
from pydantic import BaseModel


class OrdersRes(BaseModel):
    id: int
    created_date: str
    state: str
    customer_id: int
    confirmed_date: Optional[str] = None
    removed_date: Optional[str] = None
    handler_id: Optional[int] = None