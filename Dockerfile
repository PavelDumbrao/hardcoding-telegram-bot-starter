FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY pyproject.toml README.md ./
COPY bot ./bot
RUN pip install --no-cache-dir .
RUN mkdir -p /app/data
CMD ["python", "-m", "bot.main"]
