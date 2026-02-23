from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from application.dto.product import ProductCreate, ProductUpdate
from core.models import Product
from uuid import UUID
from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    async def get_by_id(
        self,
        id: UUID,
        session: AsyncSession,
    ) -> Product | None: ...

    @abstractmethod
    async def list(
        self,
        session: AsyncSession,
    ) -> List[Product]: ...

    @abstractmethod
    async def retrieve(
        self,
        id: UUID,
        session: AsyncSession,
    ) -> Product | None: ...

    @abstractmethod
    async def create(
        self,
        dto: ProductCreate,
        session: AsyncSession,
    ) -> Product: ...

    @abstractmethod
    async def update(
        self,
        product: Product,
        dto: ProductUpdate,
        session: AsyncSession,
    ) -> Product: ...

    @abstractmethod
    async def delete(
        self,
        product: Product,
        session: AsyncSession,
    ) -> None: ...
