from fastapi import APIRouter, HTTPException
from custom_exceptions.unauthorize import UnauthorizedException
from models import Orders, OrdersProducts
from services.orders_service_factory import OrdersService
from policies.authorize import LoggedInUser
from services.carts_service_factory import CartsService


router = APIRouter(prefix="/api/orders", tags=["orders"])

@router.post("/")
async def order_cart(ordersService: OrdersService, logged_in_user: LoggedInUser, cartsService: CartsService):
    if logged_in_user is None:
        raise HTTPException(404, "User not found")
    
    #Haetaan ostoskori
    cart: Orders = ordersService.get_order_by_id(logged_in_user.Id, "cart-state")
    items_in_cart: list[OrdersProducts] = cartsService.get_items_in_cart(cart.Id)
    
    #Lähetetään uusi tilaus
    sent_order = ordersService.send_order(logged_in_user.Id)
    #Lisätään ostoskorin tavarat tilaukseen ja poistetaan ostoskorista
    for item in items_in_cart:
        cartsService.add_items_to_cart(
            order_id=sent_order.Id,
            product_id=item.ProductId,
            unit_amount=item.UnitCount,
            unit_price=item.UnitPrice
        )
        cartsService.delete_items_from_cart(
            order_id=item.OrderId,
            product_id=item.ProductId
        )
    #Poistetaan ostoskori
    ordersService.delete_users_order(logged_in_user.Id, state="cart-state")

@router.post("/{order_id}/confirm")
async def confirm_order(order_id: int, orderService: OrdersService, logged_in_user: LoggedInUser):
    if logged_in_user.Role != "Admin":
        raise UnauthorizedException()
    orderService.confirm_order(order_id, logged_in_user.Id)