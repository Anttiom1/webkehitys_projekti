from dtos.Categories import AddCategoryReq, CategoryUpdateReq
from services.categories_service_base import CategoriesServiceBase
from models import Categories, Db
from custom_exceptions.not_found import NotFoundexception


class CategoriesServiceSqlAlchemy(CategoriesServiceBase):
    def __init__(self, db: Db):
        self.context = db
        
    def get_all(self):
        return self.context.query(Categories).all()
    
    def update_category(self, id, updateReq: CategoryUpdateReq ) -> Categories:
        category = self.context.query(Categories).filter(Categories.Id == id).first()
        if not category:
            raise NotFoundexception()

        if updateReq.name is not None:
            category.Name = updateReq.name
        if updateReq.description is not None:
            category.Description = updateReq.description
        
        self.context.commit()
        
        self.context.refresh(category)
        return category
        
        
    def add_category(self, addCategoryReq: AddCategoryReq, user_id:int) -> Categories:
        new_category = Categories(
            Name=addCategoryReq.name,
            UserId= user_id,
            Description=addCategoryReq.description
        )

        self.context.add(new_category)
        self.context.commit()

        self.context.refresh(new_category)

        return new_category
    
    def delete_category(self, id: int):
        try:
            category = self.context.query(Categories).filter(Categories.Id == id).first()
            self.context.delete(category)
            self.context.commit()
        except Exception as e:
            self.context.rollback()
            raise e