from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.fsm.storage.redis import RedisStorage
import redis.asyncio as redis


load_dotenv()
TOKEN = getenv("TOKEN")
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
        BotCommand(command='start', description='Перезапустить бота'),
        BotCommand(command='laws', description='Юридические вопросы: квартира, льготы, выплаты и пр.'),
        BotCommand(command='edu', description='Образование'),
        BotCommand(command='health', description='Здоровье (и что делать, если заболел)'),
        BotCommand(command='work', description='Работа и деньги'),
        BotCommand(command='room', description='Жизнь в общежитии колледжа/вуза'),
        BotCommand(command='flat', description='Жизнь в своей квартире'),
        BotCommand(command='psy', description='Психологическая поддержка'),
        BotCommand(command='room', description='Еда: что покупать и как готовить'),
        ]
    await bot.set_my_commands(commands_list, BotCommandScopeDefault())
