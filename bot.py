# import telebot
# from database import init_db, add_user, get_user

# TOKEN = '8013179965:AAET8ge9awyrenWH83Ns5w-a_PmyZ-VDi3w'
# bot = telebot.TeleBot(TOKEN)

# init_db()

# @bot.message_handler(commands=['start'])
# def start(message):
#     user = get_user(message.from_user.id)
#     if user:
#         bot.send_message(message.chat.id, f'Добро пожаловать обратно, {user[2]}!')
#     else:
#         bot.send_message(message.chat.id, 'Привет! Давай зарегистрируемся. Введи своё имя:')
#         bot.register_next_step_handler(message, ask_name)

# def ask_name(message):
#     name = message.text
#     bot.send_message(message.chat.id, 'Отлично! Теперь введи свой возраст:')
#     bot.register_next_step_handler(message, ask_age, name)

# def ask_age(message, name):
#     try:
#         age = int(message.text)
#         add_user(message.from_user.id, name, age)
#         bot.send_message(message.chat.id, f'Регистрация завершена! Привет, {name}, {age} лет.')
#     except ValueError:
#         bot.send_message(message.chat.id, 'Возраст должен быть числом. Попробуй снова.')
#         bot.register_next_step_handler(message, ask_age, name)

# bot.polling()

import time
import telebot
from database import init_db, add_user, get_user
from requests.exceptions import ReadTimeout

TOKEN = '8013179965:AAET8ge9awyrenWH83Ns5w-a_PmyZ-VDi3w'
bot = telebot.TeleBot(TOKEN)

init_db()

@bot.message_handler(commands=['start'])
def start(message):
    user = get_user(message.from_user.id)
    if user:
        bot.send_message(message.chat.id, f'Добро пожаловать обратно, {user[2]}!')
    else:
        bot.send_message(message.chat.id, 'Привет! Давай зарегистрируемся. Введи своё имя:')
        bot.register_next_step_handler(message, ask_name)

def ask_name(message):
    name = message.text
    bot.send_message(message.chat.id, 'Отлично! Теперь введи свой возраст:')
    bot.register_next_step_handler(message, ask_age, name)

def ask_age(message, name):
    try:
        age = int(message.text)
        add_user(message.from_user.id, name, age)
        bot.send_message(message.chat.id, f'Регистрация завершена! Привет, {name}, {age} лет.')
    except ValueError:
        bot.send_message(message.chat.id, 'Возраст должен быть числом. Попробуй снова.')
        bot.register_next_step_handler(message, ask_age, name)

while True:
    try:
        bot.polling(non_stop=True, interval=1, timeout=60, long_polling_timeout=20)
    except ReadTimeout:
        print("Произошёл таймаут. Перезапуск...")
        time.sleep(5)  # Подождать перед повторным запуском
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)

