from typing import List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.dto.category import CategoryCreate, CategoryUpdate
from core.models import Category
from domain.repositories import CategoryRepository


class InMemoryCategoryRepository(CategoryRepository):
    async def get_by_id(
        self,
        id: UUID,
        session: AsyncSession,
    ) -> Category | None:
        return await session.get(Category, id)

    async def retrieve(
        self,
        id: UUID,
        session: AsyncSession,
    ) -> Category | None:
        return await self.get_by_id(
            id=id,
            session=session,
        )

    async def list(
        self,
        session: AsyncSession,
    ) -> List[Category]:
        stmt = select(Category).order_by(Category.id)
        categories = await session.scalars(stmt)

        return list(categories)

    async def create(
        self,
        dto: CategoryCreate,
        session: AsyncSession,
    ) -> Category:
        category = Category(**dto.model_dump())

        session.add(category)

        await session.commit()
        await session.refresh(category)

        return category

    async def update(
        self,
        category: Category,
        dto: CategoryUpdate,
        session: AsyncSession,
    ) -> Category:
        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(category, key, value)

        await session.commit()

        return category

    async def delete(
        self,
        category: Category,
        session: AsyncSession,
    ) -> None:
        await session.delete(category)

        await session.commit()

        return None


category_repo = InMemoryCategoryRepository()
