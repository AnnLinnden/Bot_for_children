from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

flat_router = Router()


@flat_router.message(Command('food'))
async def flat_qa(message: Message):
    await message.answer("")
