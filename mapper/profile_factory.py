from typing import Type


from pydantic import BaseModel


from mapper.products_profile import ProductsProfile
from mapper.user_profile import UserProfile


def create_user_profile(_type: Type[BaseModel]):
    return UserProfile(_type)

def create_products_profile(_type: Type[BaseModel]):
    return ProductsProfile(_type)