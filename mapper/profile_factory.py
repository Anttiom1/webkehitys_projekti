from typing import Type


from pydantic import BaseModel

from mapper.cart_profile import CartProfile
from mapper.categories_profile import CategoriesProfile
from mapper.orders_profile import OrdersProfile
from mapper.products_profile import ProductsProfile
from mapper.user_profile import UserProfile


def create_user_profile(_type: Type[BaseModel]):
    return UserProfile(_type)

def create_products_profile(_type: Type[BaseModel]):
    return ProductsProfile(_type)

def create_categories_profile(_type: Type[BaseModel]):
    return CategoriesProfile(_type)

def create_orders_profile(_type: Type[BaseModel]):
    return OrdersProfile(_type)

def create_cart_profile(_type: Type[BaseModel]):
    return CartProfile(_type)