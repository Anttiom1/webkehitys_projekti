from fastapi import APIRouter,  HTTPException
from dtos.Cart import AddItemsToCartReq, UpdateItemsInCartReq
from policies.authorize import LoggedInUser
from services.orders_service_factory import OrdersService
from services.carts_service_factory import CartsService
from services.products_service_factory import ProductsService
from mapper.mapper import ResponseMapper

router = APIRouter(prefix="/api/cart", tags=["cart"])

@router.post("/items", status_code=201)
async def add_item_to_cart(cartsService: CartsService, ordersService: OrdersService, productsService: ProductsService, items: AddItemsToCartReq, logged_in_user: LoggedInUser, mapper: ResponseMapper):
    if logged_in_user is None:
        raise HTTPException(404, "user not found")
    #check it user already has order
    order = ordersService.get_order_by_id(logged_in_user.Id, "cart-state")
    if order is None:
        order = ordersService.create_order(customer_id=logged_in_user.Id, state="cart-state")
    
    product = productsService.get_product_by_id(items.product_id)
    
    products_in_cart = cartsService.add_items_to_cart(order.Id, items.product_id, items.unit_count, product.UnitPrice)
    return mapper.map("cart_dto", products_in_cart)

@router.delete("/items/{product_id}")
async def delete_items_from_cart(cartsService: CartsService, ordersService: OrdersService, product_id: int, logged_in_user: LoggedInUser):
    if logged_in_user is None:
        raise HTTPException(404, "user not found")
    order = ordersService.get_order_by_id(logged_in_user.Id, "cart-state")
    if order is None:
        raise HTTPException(404, "order not found")
    cartsService.delete_items_from_cart(product_id, order.Id)
    
@router.patch("/items/{product_id}")
async def update_items_in_cart(cartsService: CartsService, ordersService: OrdersService, product_id: int, updateReq: UpdateItemsInCartReq, logged_in_user: LoggedInUser, mapper: ResponseMapper):
    if logged_in_user is None:
        raise HTTPException(404, "user not found")
    order = ordersService.get_order_by_id(logged_in_user.Id, "cart-state")
    if order is None:
        raise HTTPException(404, "orderasd not found")
    updated_cart = cartsService.update_items_in_cart(product_id, updateReq.unit_count, order.Id,)
    return mapper.map("cart_dto", updated_cart)
