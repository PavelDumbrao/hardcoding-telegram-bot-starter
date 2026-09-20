from aiogram import F, Router
from aiogram.types import Message

from bot.analytics import track_event
from bot.config import Settings

router = Router(name="common")


@router.message(F.text == "Что умеет бот")
async def about_handler(message: Message, settings: Settings) -> None:
    await track_event(
        settings.db_path,
        message.from_user.id if message.from_user else None,
        "menu_about_clicked",
    )
    await message.answer(
        "Это стартовый шаблон. Передай проект Codex или Claude Code, "
        "и агент добавит нужные функции под твою задачу."
    )


@router.message(F.text == "Помощь")
async def menu_help_handler(message: Message, settings: Settings) -> None:
    await track_event(
        settings.db_path,
        message.from_user.id if message.from_user else None,
        "menu_help_clicked",
    )
    await message.answer("Напиши /help или опиши, что хочешь сделать.")


@router.message(F.text)
async def fallback_handler(message: Message, settings: Settings) -> None:
    await track_event(
        settings.db_path,
        message.from_user.id if message.from_user else None,
        "text_message_received",
    )
    await message.answer(
        "Я получил сообщение. Сейчас здесь заглушка. ИИ-агент заменит её на бизнес-логику."
    )
