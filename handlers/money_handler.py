from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

money_router = Router()


@money_router.message(Command('money'))
async def money_qa(message: Message):
    await message.answer("")
