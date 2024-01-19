from typing import Optional

from fastapi import APIRouter, Depends

from src.apps.products.application.use_cases import CreateProduct, SearchProducts
from src.apps.products.domain.models import Product, ProductSchema

from .schema import (
    CreateProductReq,
    CreateProductRes,
    SearchProductsRes,
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


@router.get("/search")
async def search(
    use_case: SearchProducts = Depends(SearchProducts),
    query: Optional[str] = None,
):
    return SearchProductsRes(products=[prd async for prd in use_case.execute(query)])
