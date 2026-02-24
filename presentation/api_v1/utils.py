from uuid import UUID
from infrastructure.repositories import product_repo
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status


async def check_unique_product_fields(
    session: AsyncSession,
    title: str | None,
    id: UUID | None = None,
) -> None:
    product = await product_repo.check_unique_fields(
        id=id,
        title=title,
        session=session,
    )

    if product is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product name not unique",
        )

    return None
