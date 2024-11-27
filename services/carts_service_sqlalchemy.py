from services.carts_service_base import CartsServiceBase
from models import Db, OrdersProducts



class CartsServiceSqlAlchemy(CartsServiceBase):
    def __init__(self, db: Db):
        self.context = db
        
    def add_items_to_cart(self, order_id: int, product_id: int, unit_amount: int, unit_price: int) -> OrdersProducts:
        products = OrdersProducts(
            OrderId = order_id,
            ProductId = product_id,
            UnitCount = unit_amount,
            UnitPrice = unit_price
        )
        
        self.context.add(products)
        self.context.commit()
        return products

