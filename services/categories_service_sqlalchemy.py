from services.categories_service_base import CategoriesServiceBase
from models import Categories, Db


class CategoriesServiceSqlAlchemy(CategoriesServiceBase):
    def __init__(self, db: Db):
        self.context = db
        
    def get_all(self):
        return self.context.query(Categories).all()