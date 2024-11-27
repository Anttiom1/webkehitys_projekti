from fastapi import APIRouter
from dtos.Products import ProductsRes
from services.products_service_factory import ProductsService
from mapper.mapper import ResponseMapper

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/")
async def get_all_products(service: ProductsService, mapper: ResponseMapper) -> list[ProductsRes]:
    products = service.get_all()
    return mapper.map("products_dto", products)

@router.get("/categories/{id}")
async def get_products_by_id(service: ProductsService, mapper: ResponseMapper, id: int) -> list[ProductsRes]:
    products = service.get_products_by_category_id(id)
    return mapper.map("products_dto", products)
