import os
token = os.getenv('MY_TOKEN')
channel_test = '@testramec'
#channel_tt = '@ramec_tt'
#channel_fb = '@ramec_football'
from telebot import TeleBot, types
bot = TeleBot(token=token)
ques_tt='✅ Запись на следующие тренировки 🏓'
list_tt = ['ПН - 18:00 стол 1-2', 'ЧТ - 18:30 стол 1-2', 'ПТ - 18:00 стол 1-2', 'Следить 🔍']
ques_fb='✅ Кто в этот четверг идёт на футбол? ⚽'
list_fb = ['🏃‍♂️', '🏃‍♂️🏃‍♂️', '🏃‍♂️🏃‍♂️🏃‍♂️', '🙅‍♂️']
bot.send_poll(channel_test, ques_tt, list_tt, False,'regular', True)
bot.send_poll(channel_test, ques_fb, list_fb, False,'regular', True)
