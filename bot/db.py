from __future__ import annotations

from pathlib import Path

import aiosqlite


async def init_db(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    async with aiosqlite.connect(path) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                telegram_id INTEGER PRIMARY KEY,
                username TEXT,
                full_name TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.commit()


async def upsert_user(path: Path, telegram_id: int, username: str | None, full_name: str) -> None:
    async with aiosqlite.connect(path) as db:
        await db.execute("""
            INSERT INTO users (telegram_id, username, full_name) VALUES (?, ?, ?)
            ON CONFLICT(telegram_id) DO UPDATE SET
                username=excluded.username, full_name=excluded.full_name
        """, (telegram_id, username, full_name))
        await db.commit()
