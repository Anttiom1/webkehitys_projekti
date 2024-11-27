import abc

from models import Products


class ProductsServiceBase(abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> list[Products]:
        raise NotImplementedError()