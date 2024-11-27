from typing import Annotated

from fastapi import Depends

from models import Db


from services.user_service_base import UserServiceBase
from services.user_service_sqlalchemy import UserServiceSQLAlchemy



def init_user_service(context: Db):
    return UserServiceSQLAlchemy(context)


UserService = Annotated[UserServiceBase, Depends(init_user_service)]

