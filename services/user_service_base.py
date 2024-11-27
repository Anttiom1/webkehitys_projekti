import abc

from dtos.Users import AddUserReq, LoginReq
from models import Users
from tools.token_tool_base import TokenToolBase

class UserServiceBase(abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> list[Users]:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, req: AddUserReq) -> Users:
        raise NotImplementedError()

    @abc.abstractmethod
    def login(self, req: LoginReq, token: TokenToolBase) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_user_by_id(self, user_id: int) -> Users:
        raise NotImplementedError()
    
