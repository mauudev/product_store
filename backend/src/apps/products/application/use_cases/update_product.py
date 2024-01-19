from fastapi import HTTPException

from src.apps.products.domain.models import Product, ProductSchema
from src.modules.shared.database import AsyncSession


class UpdateProduct:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(
        self, product_id: int, product_name: str, stock: int, product_image: str
    ) -> ProductSchema:
        async with self.async_session as session:
            product = await Product.read_by_id(session, product_id)
            if not product:
                raise HTTPException(status_code=404)
            await product.update(session, product_name, stock, product_image)
            await session.refresh(product)
            return ProductSchema.model_validate(product)
