from core.models import Category
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UUID, ForeignKey, String, Numeric
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Category


class Product(Base):
    __tablename__ = "products"

    title: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(
        String(1024),
        nullable=True,
    )
    url: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )
    price: Mapped[float] = mapped_column(
        Numeric(precision=10, scale=2),
        nullable=True,
    )
    category_id: Mapped[UUID] = mapped_column(ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship(back_populates="products")
