from bot.keyboards import main_keyboard


def test_main_keyboard_has_buttons() -> None:
    keyboard = main_keyboard()
    labels = [button.text for row in keyboard.keyboard for button in row]
    assert "Что умеет бот" in labels
    assert "Помощь" in labels
