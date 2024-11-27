import abc

from models import Categories


class CategoriesServiceBase(abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> list[Categories]:
        raise NotImplementedError()
