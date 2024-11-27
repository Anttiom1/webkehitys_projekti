from fastapi import APIRouter
from models import Orders, OrdersProducts
from policies.authorize import LoggedInUser
from services.orders_service_factory import OrdersService
from services.carts_service_factory import CartsService

router = APIRouter(prefix="/api/account", tags=["account"])

@router.delete("/orders/{id}")
async def delete_order(ordersService: OrdersService, cartsService: CartsService, logged_in_user: LoggedInUser):
    cart: Orders = ordersService.get_order_by_id(logged_in_user.Id, "ordered-state")
    items_in_cart: list[OrdersProducts] = cartsService.get_items_in_cart(cart.Id)
    for item in items_in_cart: 
        cartsService.delete_items_from_cart(
            order_id=item.OrderId,
            product_id=item.ProductId
        )
    ordersService.delete_users_order(logged_in_user.Id, state="ordered-state")