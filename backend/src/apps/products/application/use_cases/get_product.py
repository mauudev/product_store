from fastapi import HTTPException

from src.apps.products.domain.models import Product, ProductSchema
from src.modules.shared.database import AsyncSession


class GetProduct:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self, product_id: int) -> ProductSchema:
        async with self.async_session as session:
            product = await Product.read_by_id(session, product_id)
            return ProductSchema.model_validate(product)
