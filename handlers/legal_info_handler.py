from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

law_router = Router()


@law_router.message(Command('law'))
async def law_qa(message: Message):
    await message.answer("")
