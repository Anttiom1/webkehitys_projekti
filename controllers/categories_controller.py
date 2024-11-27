from fastapi import APIRouter, HTTPException
from custom_exceptions.not_found import NotFoundexception
from dtos.Categories import CategoriesRes, CategoryUpdateReq
from policies.authorize import LoggedInUser
from services.categories_service_factory import CategoriesService
from mapper.mapper import ResponseMapper
from response_handlers.user_res_handler import UserResResponseHandler

router = APIRouter(prefix="/api/categories", tags=["categories"])

@router.get("/")
async def get_all_categories(service: CategoriesService, mapper: ResponseMapper) -> list[CategoriesRes]:
    categories = service.get_all()
    return mapper.map("categories_dto", categories)

@router.patch("/{id}")
async def update_category(service: CategoriesService, id: int, logged_in_user: LoggedInUser, res_handler: UserResResponseHandler, categoryUpdateReq: CategoryUpdateReq):
    service.update_category(id, categoryUpdateReq)
