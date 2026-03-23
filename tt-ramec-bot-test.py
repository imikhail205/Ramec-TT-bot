import os
token = os.getenv('MY_TOKEN')

channel_test = '@testramec'
#channel_tt = '@ramec_tt'
#channel_fb = '@ramec_football'
from telebot import TeleBot, types
#from settings import *
from time import sleep
from datetime import datetime, timedelta 
from threading import Thread

bot = TeleBot(token=token)
posts = {}
action = ''
new_post = []
def sleep_poster(hour, minute, channel_test):
    ques_tt='✅ Запись на следующие тренировки 🏓'
    list_tt = ['ПН - 18:00 стол 1-2', 'ЧТ - 18:30 стол 1-2', 'ПТ - 18:00 стол 1-2', 'Следить 🔍']
    ques_fb='✅ Кто в этот четверг идёт на футбол? ⚽'
    list_fb = ['🏃‍♂️', '🏃‍♂️🏃‍♂️', '🏃‍♂️🏃‍♂️🏃‍♂️', '🙅‍♂️']
    #while True:
        #if time.now().hour == hour) & (datetime.now().minute == minute) & (datetime.now().weekday() == 6):
            bot.send_poll(channel_test, ques_tt, list_tt, False,'regular', True)
            #bot.send_message(channel,'Всем привет! Я буду публиковать опросы, больше ничего не умею)')
     #       sleep(60)
        #elif (datetime.now().hour == 9) & (datetime.now().minute == 30) & (datetime.now().weekday() == 2):
            bot.send_poll(channel_test, ques_fb, list_fb, False,'regular', True)
            #bot.send_message(channel_fb,'Всем привет! Я буду публиковать опросы, больше ничего не умею)')
      #      sleep(60)
        #else:
       #     sleep(60)
hour = 18
minute = 00
identity = datetime.now().microsecond
posts[identity] = Thread(target=sleep_poster, args=[hour, minute, channel_test])
posts[identity].run()