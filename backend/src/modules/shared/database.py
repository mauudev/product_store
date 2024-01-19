from asyncio import current_task
from contextlib import asynccontextmanager
from datetime import datetime
from functools import cache
from typing import Annotated, AsyncContextManager, AsyncIterator, Callable

from fastapi import Depends
from sqlalchemy import MetaData, QueuePool
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.settings import APP_SETTINGS

from .logger import logger

# ------------------------------------------------------------
# Base entity definition
# ------------------------------------------------------------
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    __abstract__ = True
    metadata = MetaData(naming_convention=convention)  # type: ignore


class Entity(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        "id", autoincrement=True, nullable=False, unique=True, primary_key=True
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, onupdate=datetime.utcnow
    )


# ------------------------------------------------------------
# Engine build
# ------------------------------------------------------------
@cache
def build_async_engine() -> Engine:
    return create_async_engine(
        APP_SETTINGS.DATABASE_URL_ASYNC,
        poolclass=QueuePool,
        pool_size=int(APP_SETTINGS.DATABASE_POOL_SIZE),
    )


# ------------------------------------------------------------
# Session factory
# ------------------------------------------------------------
@cache
def async_session_factory() -> Callable[[], AsyncSession]:
    logger.debug("Creating DB AsyncSession ..")
    AsyncScopedSession = async_scoped_session(
        async_sessionmaker(
            bind=build_async_engine(),
            autocommit=False,
            autoflush=True,
            future=True,
            expire_on_commit=False,
        ),
        scopefunc=current_task,
    )
    return AsyncScopedSession


# ------------------------------------------------------------
# Session providers
# ------------------------------------------------------------
@asynccontextmanager
async def async_db_session() -> AsyncContextManager[AsyncSession]:
    session: AsyncSession = async_session_factory()()
    try:
        yield session

    except Exception as e:
        logger.error("Database error, rolling back", exc_info=True)
        await session.rollback()
        raise e

    finally:
        logger.debug("Closing DB session ..")
        await session.close()


AsyncSession = Annotated[AsyncContextManager[AsyncSession], Depends(async_db_session)]
