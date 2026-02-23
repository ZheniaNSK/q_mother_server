from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from . import Product


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(255), unique=True)

    products: Mapped[List["Product"]] = relationship(back_populates="category")
