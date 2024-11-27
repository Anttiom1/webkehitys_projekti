import abc

from models import Products


class ProductsServiceBase(abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> list[Products]:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def get_products_by_category_id(self, id: int) -> list[Products]:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def get_product_by_id(self, id: int) -> Products:
        raise NotImplementedError