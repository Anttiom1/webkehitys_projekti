from fastapi import APIRouter
from dtos.Products import ProductsRes
from services.products_service_factory import ProductsService
from mapper.mapper import ResponseMapper

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/")
def get_all_products(service: ProductsService, mapper: ResponseMapper) -> list[ProductsRes]:
    products = service.get_all()
    return mapper.map("products_dto", products)
