from typing import Annotated

from fastapi import Depends
from services.products_service_base import ProductsServiceBase
from services.products_service_sqlalchemy import ProductsServiceSqlAlchemy
from models import Db


def init_products_service(context: Db):
   return ProductsServiceSqlAlchemy(context)


ProductsService = Annotated[ProductsServiceBase, Depends(init_products_service)]