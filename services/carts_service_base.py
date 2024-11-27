import abc

from models import OrdersProducts


class CartsServiceBase(abc.ABC):
    @abc.abstractmethod
    def add_items_to_cart(self, order_id, product_id: int, unit_amount: int, unit_price) -> OrdersProducts:
        raise NotImplementedError()