from services.categories_service_base import CategoriesServiceBase
from models import Categories, Db
from custom_exceptions.not_found import NotFoundexception


class CategoriesServiceSqlAlchemy(CategoriesServiceBase):
    def __init__(self, db: Db):
        self.context = db
        
    def get_all(self):
        return self.context.query(Categories).all()
    
    def update_category(self, id, updateReq) -> Categories:
        try:
            category = self.context.query(Categories).filter(Categories.Id == id).first()
            for key, value in updateReq.__dict__.items():
                if value is not None:
                    setattr(category, key, value)
            self.context.commit()
            self.context.refresh(category)
            return category
        except NotFoundexception:
            raise
        except Exception as e:
            self.context.rollback()
            raise e
        
        