from fastapi import HTTPException

from src.apps.products.domain.models import Product, ProductSchema
from src.modules.shared.database import AsyncSession


class CreateProduct:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(
        self, product_name: str, stock: int, product_image: str
    ) -> ProductSchema:
        async with self.async_session as session:
            product = await Product.create(session, product_name, stock, product_image)
            return ProductSchema.model_validate(product)
