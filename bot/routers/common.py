from aiogram import F, Router
from aiogram.types import Message

router = Router(name="common")


@router.message(F.text == "Что умеет бот")
async def about_handler(message: Message) -> None:
    await message.answer(
        "Это стартовый шаблон. Передай проект Codex или Claude Code, "
        "и агент добавит нужные функции под твою задачу."
    )


@router.message(F.text == "Помощь")
async def menu_help_handler(message: Message) -> None:
    await message.answer("Напиши /help или опиши, что хочешь сделать.")


@router.message(F.text)
async def fallback_handler(message: Message) -> None:
    await message.answer(
        "Я получил сообщение. Сейчас здесь заглушка. ИИ-агент заменит её на бизнес-логику."
    )
