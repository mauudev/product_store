from typing import List, Optional

from pydantic import BaseModel, Field
from src.apps.products.domain.models import ProductSchema


class CreateProductReq(BaseModel):
    product_name: str = Field(..., min_length=1, max_length=64)
    stock: int = Field(..., gte=0)
    product_image: str = Field(..., min_length=1, max_length=500)


class UpdateProductReq(BaseModel):
    product_name: Optional[str] = Field(None, min_length=1, max_length=64)
    stock: Optional[int] = Field(None, ge=0)
    product_image: Optional[str] = Field(None, min_length=1, max_length=500)


class ReadProductsRes(BaseModel):
    products: List[ProductSchema]
