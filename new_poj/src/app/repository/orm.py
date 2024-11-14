from src.app.config.database import async_session, async_engine, Base
from src.app.models.models import TypePackageOrm


class StartORM:

    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_type_table():
        async with async_session() as session:
            first = TypePackageOrm(nametype="одежда")
            second = TypePackageOrm(nametype="электроника")
            third = TypePackageOrm(nametype="разное")
            session.add_all([first, second, third])
            await session.commit()
