from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

room_router = Router()


@room_router.message(Command('food'))
async def room_qa(message: Message):
    await message.answer("")
