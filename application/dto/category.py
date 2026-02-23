from uuid import UUID
from pydantic import BaseModel, Field
from typing import Annotated, Optional


class CategoryBase(BaseModel):
    name: Annotated[str, Field(min_length=4, max_length=255)]


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[Annotated[str, Field(min_length=4, max_length=255)]] = None


class CategoryResponse(CategoryBase):
    id: UUID
