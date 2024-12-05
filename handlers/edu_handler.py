from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

edu_router = Router()


@edu_router.message(Command('food'))
async def edu_qa(message: Message):
    await message.answer("")
