from typing import Annotated

from fastapi import Depends
from services.orders_service_base import OrdersServiceBase
from services.orders_service_sqlalchemy import OrdersServiceSqlAlchemy
from models import Db


def init_orders_service(context: Db):
   return OrdersServiceSqlAlchemy(context)


OrdersService = Annotated[OrdersServiceBase, Depends(init_orders_service)]