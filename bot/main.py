from __future__ import annotations

import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import Settings, load_settings
from bot.db import init_db
from bot.routers import common, start


async def run_bot(settings: Settings) -> None:
    await init_db(settings.db_path)
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    dp["settings"] = settings
    dp.include_router(start.router)
    dp.include_router(common.router)
    try:
        await bot.delete_webhook(drop_pending_updates=False)
        me = await bot.get_me()
        logging.getLogger(__name__).info("Бот подключён: @%s id=%s", me.username, me.id)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


def main() -> None:
    settings = load_settings()
    logging.basicConfig(level=getattr(logging, settings.log_level, logging.INFO), format="%(asctime)s %(levelname)s %(name)s %(message)s")
    asyncio.run(run_bot(settings))


if __name__ == "__main__":
    main()
