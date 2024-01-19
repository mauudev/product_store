from fastapi import HTTPException
from src.apps.products.domain.models import Product, ProductSchema
from src.modules.shared.database import AsyncSession


class UpdateProductPartial:
    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def execute(self, product_id: int, fields: dict) -> ProductSchema:
        try:
            async with self.async_session as session:
                product = await Product.read_by_id(session, product_id)
                if not product:
                    raise HTTPException(status_code=404, detail="Product not found")
                await product.update_partial(session, fields)
                await session.refresh(product)
                return ProductSchema.model_validate(product)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
