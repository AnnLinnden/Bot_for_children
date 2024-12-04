import asyncio
from .fill_main_menu import fill_menu  # добавить сюда все остальные таблицы


async def run_all_fillers():
    await fill_menu()  # добавить вызовы всех функций из датафиллеров
