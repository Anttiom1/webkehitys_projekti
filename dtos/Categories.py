from pydantic import BaseModel


class CategoriesRes(BaseModel):
    id: int
    name: str
    user_id: int
    description: str