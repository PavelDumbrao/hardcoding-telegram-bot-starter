from bot.config import _parse_admin_ids


def test_parse_admin_ids() -> None:
    assert _parse_admin_ids("1, 2,3") == frozenset({1, 2, 3})


def test_parse_empty_admin_ids() -> None:
    assert _parse_admin_ids("") == frozenset()
