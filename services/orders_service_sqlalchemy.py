import datetime
from models import Db, Orders
from services.orders_service_base import OrdersServiceBase


class OrdersServiceSqlAlchemy(OrdersServiceBase):
    def __init__(self, db: Db):
        self.context = db
    
    def create_order(self, customer_id) -> Orders:
        order = Orders(
            CreatedDate = datetime.datetime.now(),
            State = "cart-state",
            CustomerId = customer_id
        )
        
        self.context.add(order)
        self.context.commit()
        return order
    
    def get_order_by_id(self, customer_id) -> Orders:
        order = self.context.query(Orders).filter(Orders.CustomerId == customer_id).first()
        return order