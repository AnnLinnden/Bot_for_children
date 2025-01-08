from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

future_router = Router()


@future_router.message(Command('future'))
async def future_qa(message: Message):
    await message.answer("")
