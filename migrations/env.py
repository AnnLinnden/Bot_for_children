from logging.config import fileConfig

from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from db.base import Base  # Импортируем metadata моделей
from config import database_url

# Alembic Config object
config = context.config
config.set_main_option("sqlalchemy.url", database_url)

# Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# MetaData из ваших моделей для автогенерации
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        echo=True,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)  # преобразует асинхронное соединение в синхронное.
        # Alembic выполняет свои миграции внутри синхронного блока.


def do_run_migrations(connection):
    """Настройка контекста миграции для выполнения операций.
    Это стандартный способ, рекомендованный документацией Alembic,
    чтобы избежать путаницы с асинхронным и синхронным кодом."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())
