from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

social_router = Router()


@social_router.message(Command('social'))
async def social_qa(message: Message):
    await message.answer("")
