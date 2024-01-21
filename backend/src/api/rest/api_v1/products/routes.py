from typing import Optional

from fastapi import APIRouter, Depends
from fastapi_pagination import Page, add_pagination, paginate
from src.apps.products.application.use_cases import (
    CreateProduct,
    GetProduct,
    ListProducts,
    UpdateProduct,
    UpdateProductPartial,
)
from src.apps.products.domain.models import Product, ProductSchema

from .schema import CreateProductReq, ReadProductsRes, UpdateProductReq

router = APIRouter(prefix="/products")


@router.post("/create", response_model=ProductSchema)
async def create(
    data: CreateProductReq,
    use_case: CreateProduct = Depends(CreateProduct),
):
    return await use_case.execute(data.product_name, data.stock, data.product_image)


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int, use_case: GetProduct = Depends(GetProduct)):
    return await use_case.execute(product_id)


@router.get("/", response_model=Page[ProductSchema])
async def all_products(
    use_case: ListProducts = Depends(ListProducts),
    name: Optional[str] = None,
):
    return paginate([prd async for prd in use_case.execute(name)])


@router.put(
    "/{product_id}",
    response_model=ProductSchema,
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


@router.patch(
    "/{product_id}",
    response_model=ProductSchema,
)
async def partial_update(
    product_id: int,
    fields: dict,
    use_case: UpdateProductPartial = Depends(UpdateProductPartial),
):
    return await use_case.execute(product_id, fields)
