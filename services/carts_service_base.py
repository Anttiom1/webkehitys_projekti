import abc

from models import OrdersProducts


class CartsServiceBase(abc.ABC):
    @abc.abstractmethod
    def add_items_to_cart(self, order_id, product_id: int, unit_amount: int, unit_price) -> OrdersProducts:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def delete_items_from_cart(self, product_id: int, order_id: int) -> OrdersProducts:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def update_items_in_cart(self, product_id: int, unit_count: int, order_id: int) -> OrdersProducts:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def get_item_in_cart(self, product_id: int, order_id:int) -> OrdersProducts:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def get_items_in_cart(self, order_id:int) -> list[OrdersProducts]:
        raise NotImplementedError()
    
    
    