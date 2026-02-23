from typing import Annotated
from uuid import UUID
from fastapi import Depends, Path, status, HTTPException
from core.models import Product
from infrastructure.repositories import product_repo
from core import db_helper
from sqlalchemy.ext.asyncio import AsyncSession


async def product_by_id(
    id: Annotated[UUID, Path()],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    product = await product_repo.retrieve(
        id=id,
        session=session,
    )

    if product is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            f"Product by id {id} not found",
        )

    return product
