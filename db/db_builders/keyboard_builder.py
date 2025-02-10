from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json


class InlineKeyboardBuilder:
    def __init__(self, keyboard_data: str):  # мы забираем json, но PostgreSQL хранит его как str
        self.keyboard_data = json.loads(keyboard_data)  # преобразуем строку в объект Python: list[list[dict]]

    def building_inline_keyboard(self) -> InlineKeyboardMarkup:
        """Создает объект инлайн-клавиатуры из json, хранящегося в БД.
        Готовую клавиатуру можно прикрепить к сообщению с помощью
        await message.answer("Текст", reply_markup=building_inline_keyboard())"""
        keyboard = []
        for row in self.keyboard_data:  # разбиваем построчно, берем отдельно каждый list[dict]
            buttons = [
                InlineKeyboardButton(
                    text=button['text'],
                    callback_data=button['callback_data']
                )
                for button in row
            ]  # создаем именно список, потому что инлайн-клава - список InlineKeyboardButton (список списков)
            keyboard.append(buttons)
        return InlineKeyboardMarkup(inline_keyboard=keyboard)
    # Как json хранится в БД (список списков):
    # [
    #         [{"text": "Я потерял паспорт", "callback_data": "lost_passport"}],
    #         [{"text": "Как оформить инвалидность", "callback_data": "apply_disability"}]
    # ]




