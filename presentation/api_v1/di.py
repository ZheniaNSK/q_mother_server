from typing import Annotated
from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Category
from infrastructure import category_repo
from core import db_helper
from uuid import UUID


async def category_by_id(
    id: Annotated[UUID, Path()],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Category:
    category = await category_repo.retrieve(
        id=id,
        session=session,
    )

    if category is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            f"Category by id {id} not found",
        )

    return category
