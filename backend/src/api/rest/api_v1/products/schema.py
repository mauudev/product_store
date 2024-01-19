from typing import List

from pydantic import BaseModel, Field

from src.apps.products.domain.models import ProductSchema


class ProductBase(BaseModel):
    product_name: str = Field(..., min_length=1, max_length=64)
    stock: int = Field(..., gte=0)
    product_image: str = Field(..., min_length=1, max_length=500)


class CreateProductReq(ProductBase):
    pass


class CreateProductRes(ProductBase):
    id: int


class UpdateProductReq(ProductBase):
    id: int


class UpdateProductRes(ProductBase):
    pass


class ReadAllProductsRes(BaseModel):
    products: list


class SearchProductsRes(BaseModel):
    products: List[ProductSchema]


class SearchProductsRes(BaseModel):
    products: List[ProductSchema]
