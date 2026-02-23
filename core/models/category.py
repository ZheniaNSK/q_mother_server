from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(255), unique=True)
