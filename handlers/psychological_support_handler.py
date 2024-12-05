from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

psy_router = Router()


@psy_router.message(Command('food'))
async def psy_qa(message: Message):
    await message.answer("")
