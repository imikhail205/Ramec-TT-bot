import os
token = os.getenv('MY_TOKEN')
channel_tt = '@ramec_tt'
from telebot import TeleBot, types
bot = TeleBot(token=token)
ques_tt='✅ Запись на следующие тренировки 🏓'
list_tt = ['ПН - 18:00 стол 1-2', 'ЧТ - 18:30 стол 1-2', 'ПТ - 18:00 стол 1-2', 'Следить 🔍']
bot.send_poll(channel_tt, ques_tt, list_tt, False,'regular', True)