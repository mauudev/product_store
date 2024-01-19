from __future__ import annotations

from typing import AsyncIterator

from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from src.modules.shared.database import Entity


class ProductSchema(BaseModel):
    id: int
    product_name: str
    stock: int
    product_image: str

    model_config = ConfigDict(from_attributes=True)


class Product(Entity):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        "id", autoincrement=True, nullable=False, unique=True, primary_key=True
    )
    product_name: Mapped[str] = mapped_column("product_name", nullable=False)
    stock: Mapped[int] = mapped_column("stock", nullable=False)
    product_image: Mapped[str] = mapped_column("product_image", nullable=False)

    @classmethod
    async def read_all(cls, session: AsyncSession) -> AsyncIterator[Product]:
        stmt = select(cls)
        stream = await session.stream_scalars(stmt.order_by(cls.id))
        async for row in stream:
            yield row

    @classmethod
    async def read_by_id(cls, session: AsyncSession, product_id: int) -> Product | None:
        stmt = select(cls).where(cls.id == product_id)
        return await session.scalar(stmt.order_by(cls.id))

    @classmethod
    async def search_products(
        cls, session: AsyncSession, product_name: str | None
    ) -> AsyncIterator[Product]:
        if not product_name:
            stmt = select(cls)
            stream = await session.stream_scalars(stmt.order_by(cls.id))
        else:
            stmt = select(cls).where(cls.product_name.contains(product_name))
            stream = await session.stream_scalars(stmt.order_by(cls.id))

        async for row in stream:
            yield row

    @classmethod
    async def create(
        cls, session: AsyncSession, product_name: str, stock: int, product_image: str
    ) -> Product:
        product = Product(product_name=product_name, stock=stock, product_image=product_image)
        session.add(product)
        await session.flush()
        await session.commit()
        new = await cls.read_by_id(session, product.id)
        if not new:
            raise RuntimeError()
        return new

    async def update(
        self, session: AsyncSession, product_name: str, stock: int, product_image: str
    ) -> None:
        self.product_name = product_name
        self.stock = stock
        self.product_image = product_image
        await session.flush()
        await session.commit()

    async def update_partial(self, session: AsyncSession, fields: dict) -> None:
        for key, value in fields.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)
        await session.flush()
        await session.commit()

    @classmethod
    async def delete(cls, session: AsyncSession, product: Product) -> None:
        await session.delete(product)
        await session.flush()
