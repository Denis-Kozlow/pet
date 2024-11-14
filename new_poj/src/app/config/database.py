from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.app.config.config import settings


async_engine = create_async_engine(
    url=settings.DATABASE_URL_ASYNCPG,
    echo=True,

)
async_session = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession)

sync_engine = create_engine(url=settings.DATABASE_URL_PSYCOPG, echo=True)
sync_session = sessionmaker(sync_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
