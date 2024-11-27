import datetime
from models import Db, Orders
from services.orders_service_base import OrdersServiceBase


class OrdersServiceSqlAlchemy(OrdersServiceBase):
    def __init__(self, db: Db):
        self.context = db
    
    def create_order(self, customer_id, state: str) -> Orders:
        order = Orders(
            CreatedDate = datetime.datetime.now(),
            State = state,
            CustomerId = customer_id
        )
        
        self.context.add(order)
        self.context.commit()
        return order
    
    def get_order_by_id(self, customer_id, state: str) -> Orders:
        order = self.context.query(Orders).filter(Orders.CustomerId == customer_id, Orders.State == state).first()
        return order
    
    def delete_users_cart(self, customer_id, state: str) -> Orders:
        try:
            order = self.context.query(Orders).filter(Orders.CustomerId == customer_id, Orders.State == state).first()
            self.context.delete(order)
            self.context.commit()
        except Exception as e:
            self.context.rollback()
            raise e
    
    def send_order(self, customer_id) -> Orders:
        
        sent_order = self.create_order(customer_id, "ordered-state")
        return sent_order
        
    def confirm_order(self, order_id: int, handler_id: int) -> Orders:
        order = self.context.query(Orders).filter(Orders.Id == order_id).first()

        if not order:
            raise ValueError(f"Order with ID {order_id} does not exist.")

        order.State = "Confirmed"
        order.ConfirmedDate = datetime.datetime.now()
        order.HandlerId = handler_id

        self.context.commit()

        self.context.refresh(order)

        return order