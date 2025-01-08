from config import database_manager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from db.models import MenuItem

menu_items = [
    {"command": "start", "description": "🔄 Перезапустить бота", "handler": "start_router"},
    {"command": "law", "description": "‍⚖️ Помощь юриста", "handler": "law_router"},
    {"command": "social", "description": "🤝 Соцподдержка и льготы", "handler": "social_router"},
    {"command": "edu", "description": "📚 Образование", "handler": "edu_router"},
    {"command": "health", "description": "🩺 Здоровье", "handler": "health_router"},
    {"command": "work", "description": "💼 Работа", "handler": "job_router"},
    {"command": "money", "description": "💰 Деньги", "handler": "money_router"},
    {"command": "room", "description": "🏢 Жизнь в общежитии", "handler": "room_router"},
    {"command": "flat", "description": "🏠 Жизнь в своей квартире", "handler": "flat_router"},
    {"command": "psy", "description": "️❤️ Психологическая поддержка", "handler": "psy_router"},
    {"command": "food", "description": "🥣 Еда: что покупать и как готовить", "handler": "food_router"},
    {"command": "future", "description": "🌟 Планирование будущего", "handler": "future_router"},
]


async def clear_table(session: AsyncSession, table_name: str):
    await session.execute(text(f"DELETE FROM {table_name}"))


async def fill_menu():
    async with database_manager.async_session() as session:
        async with session.begin():
            await clear_table(session, "main_menu_items")
            for item in menu_items:
                menu_item = MenuItem(
                    command=item["command"],
                    description=item["description"],
                    handler=item["handler"]
                )
                session.add(menu_item)
            session.flush()
        await session.commit()
