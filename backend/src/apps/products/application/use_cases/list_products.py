from typing import AsyncIterator

from fastapi import HTTPException

from src.apps.products.domain.models import Product, ProductSchema
from src.modules.shared.database import AsyncSession


class ListProducts:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self) -> AsyncIterator[ProductSchema]:
        try:
            async with self.async_session as session:
                async for product in Product.read_all(session):
                    yield ProductSchema.model_validate(product)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
