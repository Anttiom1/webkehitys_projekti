from pydantic import BaseModel


class ProductsRes(BaseModel):
    id: int
    name: str
    category_id: int
    unit_price: int
    description: str