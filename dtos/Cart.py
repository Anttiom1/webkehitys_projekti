from pydantic import BaseModel


class AddItemsToCartReq(BaseModel):
    product_id: int
    unit_count: int

class UpdateItemsInCartReq(BaseModel):
    unit_count: int