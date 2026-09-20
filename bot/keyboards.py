from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Что умеет бот")], [KeyboardButton(text="Помощь")]],
        resize_keyboard=True,
        input_field_placeholder="Выбери действие",
    )
