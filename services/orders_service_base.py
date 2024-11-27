import abc

from models import Orders

class OrdersServiceBase(abc.ABC):
    @abc.abstractmethod
    def create_order(self, customer_id, state: str) -> Orders:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def get_order_by_id(self, customer_id, state: str) -> Orders:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def send_order(self, customer_id) -> Orders:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def delete_users_cart(self, customer_id, state: str) -> Orders:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def confirm_order(self, order_id: int, handler_id:int) -> Orders:
        raise NotImplementedError()