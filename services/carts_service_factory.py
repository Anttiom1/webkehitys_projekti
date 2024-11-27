from typing import Annotated

from fastapi import Depends
from services.carts_service_base import CartsServiceBase
from services.carts_service_sqlalchemy import CartsServiceSqlAlchemy
from models import Db


def init_carts_service(context: Db):
   return CartsServiceSqlAlchemy(context)


CartsService = Annotated[CartsServiceBase, Depends(init_carts_service)]