from typing import List
from fastapi import APIRouter, Depends, status
from core.models import Product
from ..di import product_by_id
from application.dto.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
)
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from infrastructure.repositories import product_repo


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/{id}/", response_model=ProductResponse)
def retrieve(
    product: Product = Depends(product_by_id),
) -> Product:
    return product


@router.get("/", response_model=List[ProductResponse])
async def list(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> List[Product]:
    return await product_repo.list(
        session=session,
    )


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create(
    dto: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    return await product_repo.create(
        dto=dto,
        session=session,
    )


@router.patch("/{id}/", response_model=ProductResponse)
async def update(
    dto: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    return await product_repo.update(
        product=product,
        dto=dto,
        session=session,
    )

@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await product_repo.delete(
        product=product,
        session=session,
    )

    return None
