import asyncio
from .fill_qa_table import fill_qa_items  # добавить сюда все таблицы


async def run_all_fillers():
    await fill_qa_items()  # добавить вызовы всех функций из датафиллеров
