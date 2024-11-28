from pydantic import BaseModel


class AddItemsToCartReq(BaseModel):
    product_id: int
    unit_count: int

class UpdateItemsInCartReq(BaseModel):
    unit_count: int
    
class CartRes(BaseModel):
    order_id: int
    product_id: int
    unit_count: int
    unit_price: int