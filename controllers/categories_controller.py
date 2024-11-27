from fastapi import APIRouter
from dtos.Categories import CategoriesRes

from services.categories_service_factory import CategoriesService
from mapper.mapper import ResponseMapper

router = APIRouter(prefix="/api/categories", tags=["categories"])

@router.get("/")
async def get_all_categories(service: CategoriesService, mapper: ResponseMapper) -> list[CategoriesRes]:
    categories = service.get_all()
    return mapper.map("categories_dto", categories)