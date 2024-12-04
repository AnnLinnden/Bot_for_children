from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from .base import Base


class DatabaseManager:
    def __init__(self, database_url):
        self.engine = create_async_engine(database_url, echo=True)
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    async def initialize_database(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)  # Автоматически создаем все таблицы
