from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

job_router = Router()


@job_router.message(Command('work'))
async def job_qa(message: Message):
    await message.answer("")
