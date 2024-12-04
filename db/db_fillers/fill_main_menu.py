from config import database_manager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from db.models import MenuItem

menu_items = [
    {"command": "start", "description": "🔄 Перезапустить бота", "response": "Привет! Я готов помочь!"},
    {"command": "laws", "description": "‍⚖️ Помощь юриста", "response": "Здесь вы узнаете о льготах, выплатах и прочем."},
    {"command": "edu", "description": "📚 Образование", "response": "Помощь в выборе учебного заведения."},
    {"command": "health", "description": "🩺 Здоровье", "response": "Помощь"},
    {"command": "work", "description": "💳 Работа и деньги", "response": "Помощь в выборе"},
    {"command": "room", "description": "🏢 Жизнь в общежитии", "response": "Помощь в выборе"},
    {"command": "flat", "description": "🏠 Жизнь в своей квартире", "response": "Помощь в выборе"},
    {"command": "psy", "description": "️❤️ Психологическая поддержка", "response": "Помощь в выборе"},
    {"command": "food", "description": "🥣 Еда: что покупать и как готовить", "response": "Помощь в выборе"},
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
                    response=item["response"]
                )
                session.add(menu_item)
            session.flush()
        await session.commit()
