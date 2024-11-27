import abc

from models import Orders

class OrdersServiceBase(abc.ABC):
    @abc.abstractmethod
    def create_order(self, customer_id) -> Orders:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def get_order_by_id(self, customer_id) -> Orders:
        raise NotImplementedError()