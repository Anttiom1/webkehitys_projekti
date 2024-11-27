from typing import Annotated

from fastapi import Depends

from services.categories_service_base import CategoriesServiceBase
from services.categories_service_sqlalchemy import CategoriesServiceSqlAlchemy
from models import Db


def init_categories_service(context: Db):
   return CategoriesServiceSqlAlchemy(context)


CategoriesService = Annotated[CategoriesServiceBase, Depends(init_categories_service)]