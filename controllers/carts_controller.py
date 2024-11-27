from fastapi import APIRouter,  HTTPException
from dtos.Cart import AddItemsToCartReq
from policies.authorize import LoggedInUser
from services.orders_service_factory import OrdersService
from services.carts_service_factory import CartsService
from services.products_service_factory import ProductsService

router = APIRouter(prefix="/api/cart", tags=["cart"])

@router.post("/items", status_code=201)
async def add_item_to_cart(cartsService: CartsService, ordersService: OrdersService, productsService: ProductsService, items: AddItemsToCartReq, logged_in_user: LoggedInUser):

    #check it user already has order
    order = ordersService.get_order_by_id(logged_in_user.Id)
    if order is None:
        order = ordersService.create_order(customer_id=logged_in_user.Id)
    
    product = productsService.get_product_by_id(items.product_id)
    
    products_in_cart = cartsService.add_items_to_cart(order.Id, items.product_id, items.unit_count, product.UnitPrice)
    return products_in_cart
    
    