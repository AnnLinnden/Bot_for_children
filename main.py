import asyncio
import logging
from config import bot, dp, set_commands, database_manager
from db.db_fillers import run_all_fillers
from handlers import (food_router, room_router, edu_router, flat_router, health_router, social_router,
                      job_router, law_router, psy_router, start_router, money_router, future_router)

# Включаем логирование, пишем сразу в консоль и в файл
handler_console = logging.StreamHandler()
handler_file = logging.FileHandler('bot.log')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[handler_file, handler_console])
logger = logging.getLogger(__name__)


async def main():
    logger.info("Запускаем бота")
    dp.include_routers(food_router, room_router, edu_router, flat_router, health_router, social_router,
                       job_router, law_router, psy_router, start_router, money_router, future_router)

    # запуск в режиме long polling: при запуске бот очищает все обновления, прилетевшие, пока он не работал
    try:
        logger.info("Удаляем вебхуки, сбрасываем обновления, пришедшие за время простоя")
        await bot.delete_webhook(drop_pending_updates=True)
        logger.info("Запускаем polling")
        await dp.start_polling(bot, skip_updates=True)
        logger.info("Создаем меню с командами")
        await set_commands()
    finally:
        logger.info("Останавливаем бота")
        await bot.session.close()

asyncio.run(run_all_fillers())  # для заполнения всех баз данных
asyncio.run(main())
