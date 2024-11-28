from typing import Annotated

from fastapi.params import Depends


from dtos.Cart import CartRes
from dtos.Categories import CategoriesRes
from dtos.Orders import OrdersRes
from dtos.Products import ProductsRes
from dtos.Users import UserRes
from mapper.base_profile import BaseProfile
from mapper.profile_factory import create_cart_profile, create_categories_profile, create_orders_profile, create_products_profile, create_user_profile


class Mapper:
    # Mapper-luokka sisältää kaikki profile-objektit, sekä map-metodin
    # jossa käytetään profiilikohtaista map / map_list-metodia
    def __init__(self, profiles: dict[str: BaseProfile]) -> None:
        self.profiles = profiles

    def map(self, _type, data):
        if _type not in self.profiles.keys():
            raise Exception('Profile missing')

        if isinstance(data, list):
            return self.profiles[_type].map_list(data)
        else:
            return self.profiles[_type].map(data)


# factory mapperin luomiseen
def create_mapper() -> Mapper:
    # kun sinulle tulee lisää profiileja, lisää ne tähän
    profiles = {
        # UserDto no tietotyyppi, johon tällä profiililla (user_dto) pystyy mäppäämään
        'user_dto': create_user_profile(UserRes),
        'products_dto': create_products_profile(ProductsRes),
        'categories_dto': create_categories_profile(CategoriesRes),
        'orders_dto': create_orders_profile(OrdersRes),
        'cart_dto': create_cart_profile(CartRes)
    }
    return Mapper(profiles)

# luodaan Mapperille typealias, jota voidaan käyttää controllerissa
ResponseMapper = Annotated[Mapper, Depends(create_mapper)]
