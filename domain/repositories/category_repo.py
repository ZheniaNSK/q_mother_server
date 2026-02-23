from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from application.dto.category import CategoryCreate, CategoryUpdate
from core.models import Category
from uuid import UUID
from abc import ABC, abstractmethod


class CategoryRepository(ABC):
    @abstractmethod
    async def get_by_id(
        self,
        id: UUID,
        session: AsyncSession,
    ) -> Category | None: ...

    @abstractmethod
    async def list(
        self,
        session: AsyncSession,
    ) -> List[Category]: ...

    @abstractmethod
    async def retrieve(
        self,
        id: UUID,
        session: AsyncSession,
    ) -> Category | None: ...

    @abstractmethod
    async def create(
        self,
        dto: CategoryCreate,
        session: AsyncSession,
    ) -> Category: ...

    @abstractmethod
    async def update(
        self,
        category: Category,
        dto: CategoryUpdate,
        session: AsyncSession,
    ) -> Category: ...

    @abstractmethod
    async def delete(
        self,
        category: Category,
        session: AsyncSession,
    ) -> None: ...
