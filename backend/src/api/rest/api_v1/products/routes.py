from fastapi import APIRouter, Depends, Path, Request

from apps.products.application.use_cases.use_cases import CreateProduct
from src.apps.products.domain.models import Product, ProductSchema

from .schema import (
    CreateProductReq,
    CreateProductRes,
    UpdateProductReq,
    UpdateProductRes,
)

router = APIRouter(prefix="/products")


@router.post("/create", response_model=CreateProductRes)
async def create(
    data: CreateProductReq,
    use_case: CreateProduct = Depends(CreateProduct),
) -> ProductSchema:
    return await use_case.execute(data.product_name, data.stock, data.product_image)
