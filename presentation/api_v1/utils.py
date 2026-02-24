from uuid import UUID
from infrastructure import category_repo
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status


async def check_unique_category_fields(
    session: AsyncSession,
    name: str | None,
    id: UUID | None = None,
) -> None:
    category = await category_repo.check_unique_fields(
        id=id,
        name=name,
        session=session,
    )

    if category is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Category name not unique",
        )
    
    return None
