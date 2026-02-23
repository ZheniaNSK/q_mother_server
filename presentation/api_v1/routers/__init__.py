from fastapi import APIRouter
from .product import router as product_router


api_v1_router = APIRouter()


api_v1_router.include_router(product_router)
