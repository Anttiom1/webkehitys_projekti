from services.products_service_base import ProductsServiceBase
from models import Db, Products

class ProductsServiceSqlAlchemy(ProductsServiceBase):
    def __init__(self, db: Db):
        self.context = db
        
    def get_all(self):
        return self.context.query(Products).all()
    
    def get_products_by_category_id(self, id: int) -> list[Products]:
        return self.context.query(Products).filter(Products.CategoryId == id).all()