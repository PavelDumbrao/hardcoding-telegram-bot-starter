import json

import aiosqlite
import pytest

from bot.analytics import track_event
from bot.db import init_db


@pytest.mark.asyncio
async def test_track_event(tmp_path):
    db_path = tmp_path / "bot.sqlite3"
    await init_db(db_path)
    await track_event(db_path, 123, "bot_started", {"source": "test"})

    async with aiosqlite.connect(db_path) as db:
        cursor = await db.execute(
            "SELECT telegram_id, event_name, payload_json FROM events"
        )
        row = await cursor.fetchone()

    assert row is not None
    assert row[0] == 123
    assert row[1] == "bot_started"
    assert json.loads(row[2]) == {"source": "test"}
