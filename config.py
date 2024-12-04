from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.fsm.storage.redis import RedisStorage
import redis.asyncio as redis
import db.models
from db.storage import DatabaseManager


load_dotenv()
TOKEN = getenv("TOKEN")
database_url = getenv("DATABASE_URL")
database_manager = DatabaseManager(database_url=database_url)
async_redis_client = redis.Redis(host=getenv('HOST_REDIS'),
                                 port=int(getenv('PORT_REDIS')),
                                 decode_responses=True,
                                 username=getenv('USERNAME_REDIS'),
                                 password=getenv('PASSWORD_REDIS'))
redis_storage = RedisStorage(redis=async_redis_client)

bot = Bot(token=TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=redis_storage)


async def set_commands():
    commands_list = [
        BotCommand(command='start', description='🔄 Перезапустить бота'),
        BotCommand(command='laws', description='👨‍⚖️ Юридические вопросы: квартира, льготы, выплаты и пр.'),
        BotCommand(command='edu', description='📚 Образование: школа, колледж, вуз'),
        BotCommand(command='health', description='🩺 Здоровье (и что делать, если заболел)'),
        BotCommand(command='work', description='💳 Работа и деньги'),
        BotCommand(command='room', description='🏢 Жизнь в общежитии после выпуска'),
        BotCommand(command='flat', description='🏠 Жизнь в своей квартире'),
        BotCommand(command='psy', description='❤️ Психологическая поддержка'),
        BotCommand(command='food', description='🥣 Еда: что покупать и как готовить'),
        ]
    await bot.set_my_commands(commands_list, BotCommandScopeDefault())


async def set_commands_from_db():
    commands = await db.models.MenuItem.get_all_menu_items()  # Достаем все записи из таблицы
    commands_list = [
        BotCommand(command=item.command, description=item.description) for item in commands
    ]
    await bot.set_my_commands(commands_list, BotCommandScopeDefault())
