from typing import Optional

from fastapi import APIRouter, Depends

from src.apps.products.application.use_cases import (
    CreateProduct,
    GetProduct,
    ListProducts,
    SearchProducts,
    UpdateProduct,
)
from src.apps.products.domain.models import Product, ProductSchema

from .schema import (
    CreateProductReq,
    CreateProductRes,
    ReadProductRes,
    ReadProductsRes,
    UpdateProductReq,
    UpdateProductRes,
)

router = APIRouter(prefix="/products")


@router.post("/create", response_model=ProductSchema)
async def create(
    data: CreateProductReq,
    use_case: CreateProduct = Depends(CreateProduct),
):
    return await use_case.execute(data.product_name, data.stock, data.product_image)


@router.get("/search", response_model=ReadProductsRes)
async def search(
    use_case: SearchProducts = Depends(SearchProducts),
    query: Optional[str] = None,
):
    return ReadProductsRes(products=[prd async for prd in use_case.execute(query)])


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int, use_case: GetProduct = Depends(GetProduct)):
    return await use_case.execute(product_id)


@router.get("/", response_model=ReadProductsRes)
async def read_all(use_case: ListProducts = Depends(ListProducts)):
    return ReadProductsRes(products=[prd async for prd in use_case.execute()])


@router.put(
    "/{product_id}",
    response_model=UpdateProductRes,
)
async def update(
    data: UpdateProductReq,
    product_id: int,
    use_case: UpdateProduct = Depends(UpdateProduct),
):
    return await use_case.execute(
        product_id,
        data.product_name,
        data.stock,
        data.product_image,
    )
