# Hardcoding PRO: Telegram Bot Starter

Готовый минимальный каркас Telegram-бота для вайбкодинга.

Тебе не нужно писать проект с нуля. Нажми **Use this template**, создай свою копию репозитория, открой её в Codex / Claude Code и отдай агенту файл `PROMPT_ADAPT.md`.

## Что уже готово

- Python 3.12
- aiogram 3.31
- команды `/start` и `/help`
- простое меню
- SQLite для пользователей
- безопасная конфигурация через `.env`
- журналирование
- Docker и Docker Compose
- тесты и Ruff
- GitHub Actions
- `AGENTS.md` с правилами для ИИ-агента
- готовый промпт адаптации под бизнес

## Самый короткий путь

1. Создай бота через `@BotFather` командой `/newbot`.
2. Сохрани токен как пароль.
3. Создай копию этого репозитория через **Use this template**.
4. Открой проект в Codex или Claude Code.
5. Вставь промпт из `PROMPT_ADAPT.md`.
6. Когда агенту понадобится токен, вводи его локально в `.env` или через безопасный ввод секретов, не в обычный чат.
7. Агент сам меняет код, запускает тесты и доводит бота до рабочего состояния.

## Запуск

    cp .env.example .env
    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install -e '.[dev]'
    python -m bot.main

## Docker

    cp .env.example .env
    docker compose up -d --build
    docker compose logs -f

## Проверки

    pytest -q
    ruff check .
    python -m compileall -q bot

## Важно

Токен бота даёт полный контроль над ботом. Не коммить `.env`, не вставляй токен в обычные промпты и не публикуй его.
