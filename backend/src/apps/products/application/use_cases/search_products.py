from typing import AsyncIterator

from fastapi import HTTPException

from src.apps.products.domain.models import Product, ProductSchema
from src.modules.shared.database import AsyncSession


class SearchProducts:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self, product_name: str | None) -> AsyncIterator[ProductSchema]:
        async with self.async_session as session:
            async for product in Product.search_products(session, product_name):
                yield ProductSchema.model_validate(product)
