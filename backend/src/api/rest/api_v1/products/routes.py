from typing import Optional

import socketio
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from src.api.socketio_server import get_sio_instance
from src.apps.products.application.use_cases import (
    BuyProduct,
    CreateProduct,
    GetProduct,
    ListProducts,
    UpdateProduct,
    UpdateProductPartial,
)
from src.apps.products.domain.models import ProductSchema

from .schema import CreateProductReq, UpdateProductReq

router = APIRouter(prefix="/products")


@router.post("/create", response_model=ProductSchema)
async def create(
    data: CreateProductReq,
    use_case: CreateProduct = Depends(CreateProduct),
):
    """
    Async function to create a product using the provided data and use case.

    Args:
        data (CreateProductReq): The data for creating the product.
        use_case (CreateProduct): The use case for creating the product.

    Returns:
        The product created using the provided data and use case.
    """
    return await use_case.execute(data.product_name, data.stock, data.product_image)


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int, use_case: GetProduct = Depends(GetProduct)):
    """
    Get a product by its ID using the specified use case.

    Args:
        product_id (int): The ID of the product to retrieve.
        use_case (GetProduct): The use case for getting the product.

    Returns:
        The product retrieved by the use case.
    """
    return await use_case.execute(product_id)


@router.get("/", response_model=Page[ProductSchema])
async def all_products(
    use_case: ListProducts = Depends(ListProducts),
    name: Optional[str] = None,
):
    """
    Get all products and paginate the results based on the given parameters.

    Parameters:
        use_case (ListProducts): The use case for listing products.
        name (str, optional): The name of the product to filter by.

    Returns:
        Page[ProductSchema]: A paginated response of ProductSchema objects.
    """
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
    """
    An asynchronous function that updates a product using the given data and product ID.

    Args:
        data (UpdateProductReq): The data to update the product.
        product_id (int): The ID of the product to update.
        use_case (UpdateProduct): An instance of the UpdateProduct class.

    Returns:
        ProductSchema: The updated product data.
    """
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
    """
    Async function for partially updating a product.

    Args:
        product_id (int): The ID of the product to be updated.
        fields (dict): The fields to be updated.
        use_case (UpdateProductPartial): An instance of UpdateProductPartial.

    Returns:
        The result of the partial update operation.
    """
    return await use_case.execute(product_id, fields)


@router.patch("/{product_id}/buy/{quantity}", response_model=ProductSchema)
async def buy_product(
    product_id: int,
    quantity: int,
    use_case: BuyProduct = Depends(BuyProduct),
    sio: socketio.AsyncServer = Depends(get_sio_instance),
):
    """
    Endpoint for buying a product.

    Args:
        product_id (int): The ID of the product to be bought.
        quantity (int): The quantity of the product to be bought.
        use_case (BuyProduct, optional): An instance of the BuyProduct class. Defaults to Depends(BuyProduct).
        sio (socketio.AsyncServer, optional): An instance of the socketio.AsyncServer. Defaults to Depends(get_sio_instance).

    Returns:
        ProductSchema: The schema of the product that was bought.
    """
    product = await use_case.execute(product_id, quantity)
    await sio.emit("reply", {"productId": product.id, "newStock": product.stock})

    return product
