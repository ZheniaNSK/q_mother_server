from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel, Field
from typing import Annotated, Optional


class ProductBase(BaseModel):
    title: Annotated[str, Field(max_length=255)]
    description: Optional[Annotated[str, Field(max_length=1024)]] = None
    url: Optional[Annotated[str, Field(max_length=255)]] = None
    price: Optional[
        Annotated[Decimal, Field(gt=0, max_digits=10, decimal_places=2)]
    ] = None
    category_id: UUID


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    title: Optional[Annotated[str, Field(max_length=255)]] = None
    description: Optional[Annotated[str, Field(max_length=1024)]] = None
    url: Optional[Annotated[str, Field(max_length=255)]] = None
    price: Optional[
        Annotated[Decimal, Field(gt=0, max_digits=10, decimal_places=2)]
    ] = None
    category_id: Optional[UUID] = None


class ProductResponse(ProductBase):
    id: UUID
