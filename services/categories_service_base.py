import abc

from dtos.Categories import AddCategoryReq
from models import Categories


class CategoriesServiceBase(abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> list[Categories]:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def update_category(self, id, updateReq) -> Categories:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def add_category(self, addCategoryReq: AddCategoryReq, user_id: int) -> Categories:
        raise NotImplementedError
    
    @abc.abstractmethod
    def delete_category(self, id: int):
        raise NotImplementedError