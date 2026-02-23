from fastapi import APIRouter, Depends, status
from ..di import category_by_id
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Category
from infrastructure import category_repo
from core import db_helper
from application.dto.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)


router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/{id}/", response_model=CategoryResponse)
def retrieve(
    category: Category = Depends(category_by_id),
) -> Category:
    return category


@router.get("/", response_model=List[CategoryResponse])
async def list(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> List[Category]:
    return await category_repo.list(
        session=session,
    )


@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    dto: CategoryCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Category:
    return await category_repo.create(
        dto=dto,
        session=session,
    )


@router.patch("/{id}/", response_model=CategoryResponse)
async def update(
    dto: CategoryUpdate,
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Category:
    return await category_repo.update(
        category=category,
        dto=dto,
        session=session,
    )


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    return await category_repo.delete(
        category=category,
        session=session,
    )
