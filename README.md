# Conductor Bot

This repository contains a small Telegram bot example. It demonstrates a simple user registration flow using a SQLite database.

## Setup

1. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the bot

Run the bot script:
```bash
python bot.py
```
The bot will start polling Telegram. Use `/start` in chat with the bot to register a user.

## Example interaction

```
User: /start
Bot: Привет! Давай зарегистрируемся. Введи своё имя:
User: Алексей
Bot: Отлично! Теперь введи свой возраст:
User: 30
Bot: Регистрация завершена! Привет, Алексей, 30 лет.
```

This basic flow should help you understand how the bot works with this repository.
