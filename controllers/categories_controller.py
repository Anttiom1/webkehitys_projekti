from fastapi import APIRouter, HTTPException
from custom_exceptions.not_found import NotFoundexception
from dtos.Categories import AddCategoryReq, CategoriesRes, CategoryUpdateReq
from policies.authorize import LoggedInUser
from services.categories_service_factory import CategoriesService
from mapper.mapper import ResponseMapper
from response_handlers.user_res_handler import UserResResponseHandler
from custom_exceptions.unauthorize import UnauthorizedException

router = APIRouter(prefix="/api/categories", tags=["categories"])

@router.get("/")
async def get_all_categories(service: CategoriesService, mapper: ResponseMapper) -> list[CategoriesRes]:
    categories = service.get_all()
    return mapper.map("categories_dto", categories)

@router.patch("/{id}")
async def update_category(service: CategoriesService, id: int, logged_in_user: LoggedInUser, categoryUpdateReq: CategoryUpdateReq, mapper: ResponseMapper):
    if logged_in_user.Role != "Admin":
        raise UnauthorizedException()
    updated_category = service.update_category(id, categoryUpdateReq)
    return mapper.map("categories_dto", updated_category)
    
@router.post("/")
async def add_category(service: CategoriesService, mapper: ResponseMapper, logged_in_user: LoggedInUser, addCategoryReq: AddCategoryReq):
    if logged_in_user.Role != "Admin":
        raise UnauthorizedException()
    added_category = service.add_category(addCategoryReq, logged_in_user.Id)
    return mapper.map("categories_dto", added_category)

@router.delete("/{id}")
async def delete_category(id:int, service: CategoriesService, logged_in_user: LoggedInUser):
    if logged_in_user.Role != "Admin":
        raise UnauthorizedException()
    service.delete_category(id)