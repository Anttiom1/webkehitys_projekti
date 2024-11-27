from typing import Annotated

from fastapi import Depends
from dtos.Users import UserRes


class UserResListHandler:
    def send(self, user_list):
        user_res_list = []
        for user in user_list:
            user_res_list.append(UserRes(id=user.Id, username=user.UserName, role=user.Role))
        return user_res_list


def  init_user_list_response_handler():
    return UserResListHandler()

UserResListResponseHandler = Annotated[UserResListHandler, Depends(init_user_list_response_handler)]

class UserResHandler:
    def send(self, user):
        return UserRes(id=user.Id, username=user.UserName, role=user.Role)


def init_user_response_handler():
    return UserResHandler()

UserResResponseHandler = Annotated[UserResHandler, Depends(init_user_response_handler)]