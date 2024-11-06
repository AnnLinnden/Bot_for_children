from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message


start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Первое сообщение")
    time.sleep(3)
    await message.answer("Второе сообщение")
