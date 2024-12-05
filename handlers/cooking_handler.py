from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

food_router = Router()


@food_router.message(Command('food'))
async def food_qa(message: Message):
    await message.answer("")
