from fastapi import APIRouter
from .category import router as category_router


api_v1_router = APIRouter()


api_v1_router.include_router(category_router)
