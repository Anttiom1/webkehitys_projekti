from services.carts_service_base import CartsServiceBase
from models import Db, OrdersProducts, Products
from custom_exceptions.not_found import NotFoundexception


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
    
    def delete_items_from_cart(self, product_id: int, order_id: int) -> OrdersProducts:
        try:
            product = self.context.query(OrdersProducts).filter(OrdersProducts.ProductId == product_id, OrdersProducts.OrderId == order_id).first()
            self.context.delete(product)
            self.context.commit()
        except Exception as e:
            self.context.rollback()
            raise e
            
   
            