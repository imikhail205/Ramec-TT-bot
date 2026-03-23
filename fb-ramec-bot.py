import os
token = os.getenv('MY_TOKEN')
channel_fb = '@ramec_football'
from telebot import TeleBot, types
bot = TeleBot(token=token)
ques_fb='✅ Кто в этот четверг идёт на футбол? ⚽'
list_fb = ['🏃‍♂️', '🏃‍♂️🏃‍♂️', '🏃‍♂️🏃‍♂️🏃‍♂️', '🙅‍♂️']
bot.send_poll(channel_fb, ques_fb, list_fb, False,'regular', True)