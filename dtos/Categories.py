from pydantic import BaseModel


class CategoriesRes(BaseModel):
    id: int
    name: str
    user_id: int
    description: str
    
class CategoryUpdateReq(BaseModel):
    name: str
    description: str
    
class AddCategoryReq(BaseModel):
    name: str
    description: str