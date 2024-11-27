from typing import Annotated

from fastapi import Depends

import models
from services.user_service_base import UserServiceBase
from services.user_service_sqlalchemy import UserServiceSQLAlchemy

def init_user_service(db: models.Db):
    return UserServiceSQLAlchemy(db)

UserService = Annotated[UserServiceBase, Depends(init_user_service)]