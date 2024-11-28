from services.carts_service_base import CartsServiceBase
from models import Db, OrdersProducts, Products
from custom_exceptions.not_found import NotFoundexception


class CartsServiceSqlAlchemy(CartsServiceBase):
    def __init__(self, db: Db):
        self.context = db
        
    def add_items_to_cart(self, order_id: int, product_id: int, unit_amount: int, unit_price: int) -> OrdersProducts:
        products = OrdersProducts(
            OrderId = order_id,
            ProductId = product_id,
            UnitCount = unit_amount,
            UnitPrice = unit_price
        )
        
        self.context.add(products)
        self.context.commit()
        return products
    
    def get_item_in_cart(self, product_id: int, order_id: int) -> OrdersProducts:
        self.context.query(OrdersProducts).filter(OrdersProducts.ProductId == product_id, OrdersProducts.OrderId == order_id).first()
        
    def get_items_in_cart(self, order_id: int) -> list[OrdersProducts]:
        items_in_cart: list[OrdersProducts] = self.context.query(OrdersProducts).filter(OrdersProducts.OrderId == order_id).all()
        return items_in_cart
    
    def delete_items_from_cart(self, product_id: int, order_id: int) -> OrdersProducts:
        try:
            product = self.context.query(OrdersProducts).filter(OrdersProducts.ProductId == product_id, OrdersProducts.OrderId == order_id).first()
            self.context.delete(product)
            self.context.commit()
        except Exception as e:
            self.context.rollback()
            raise e
        
    def update_items_in_cart(self, product_id: int, unit_count: int, order_id: int) -> OrdersProducts:
        try:
            product = self.context.query(OrdersProducts).filter(
                OrdersProducts.ProductId == product_id,
                OrdersProducts.OrderId == order_id
            ).first()

            if product is None:
                raise NotFoundexception(f"Product with ID {product_id} in Order {order_id} not found.")
            product.UnitCount = unit_count  

            self.context.commit()

            self.context.refresh(product)

            return product  

        except Exception as e:
            self.context.rollback()
            raise Exception(f"Error updating items in cart: {str(e)}")
            