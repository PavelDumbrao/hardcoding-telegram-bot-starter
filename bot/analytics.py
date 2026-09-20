from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import aiosqlite


async def track_event(
    path: Path,
    telegram_id: int | None,
    event_name: str,
    payload: dict[str, Any] | None = None,
) -> None:
    async with aiosqlite.connect(path) as db:
        await db.execute(
            """
            INSERT INTO events (telegram_id, event_name, payload_json)
            VALUES (?, ?, ?)
            """,
            (
                telegram_id,
                event_name,
                json.dumps(payload or {}, ensure_ascii=False, sort_keys=True),
            ),
        )
        await db.commit()
