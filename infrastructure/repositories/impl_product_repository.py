from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from application.dto.product import ProductCreate, ProductUpdate
from core.models import Product
from domain.repositories import ProductRepository


class InMemoryProductRepository(ProductRepository):
    async def get_by_id(
        self,
        id: UUID,
        session: AsyncSession,
    ) -> Product | None:
        return await session.get(Product, id)

    async def list(
        self,
        session: AsyncSession,
    ) -> List[Product]:
        stmt = select(Product).order_by(Product.title)
        products = await session.scalars(stmt)

        return list(products)

    async def retrieve(
        self,
        id: UUID,
        session: AsyncSession,
    ) -> Product | None:
        return await self.get_by_id(
            id=id,
            session=session,
        )

    async def create(
        self,
        dto: ProductCreate,
        session: AsyncSession,
    ) -> Product:
        product = Product(**dto.model_dump())

        session.add(product)

        await session.commit()
        await session.refresh(product)

        return product

    async def update(
        self,
        product: Product,
        dto: ProductUpdate,
        session: AsyncSession,
    ) -> Product:
        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(product, key, value)

        await session.commit()

        return product

    async def delete(
        self,
        product: Product,
        session: AsyncSession,
    ) -> None:
        await session.delete(product)

        await session.commit()

        return None


product_repo = InMemoryProductRepository()
