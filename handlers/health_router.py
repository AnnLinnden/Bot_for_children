from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

health_router = Router()


@health_router.message(Command('health'))
async def health_qa(message: Message):
    await message.answer("")
