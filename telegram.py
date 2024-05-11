import os
import os
import time
import requests
import json
import shutil
import telegram
import colorama
import os
import zipfile
import subprocess
from colorama import Fore
import random
import string
from random import choice as densor
import datetime

colorama.init(autoreset=True)


print(Fore.BLUE+"""
[  Telegram - DENS0R  ] 
[  Instagram - 6gr8   ] 
[  Github - 6gr8      ] 
[  Coded By Mr DeNsor ]
""")

import telebot
import random
import string

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

stopin = False

@bot.message_handler(commands=['start', 'num', 'user', 'stop','password','visa'])
def bott(message):
    global stopin
    command = message.text.split()[0]
    if command == '/start':
        bot.send_message(message.chat.id, f'Hey , \n/num [Phone Numbers Maker] \n/user [Users Maker] \n/password [Passwords Maker] \n/visa [ Visa Maker] \n/stop [Stop]')
    elif command == '/num':
        bot.send_message(message.chat.id, '...')
        global stopin
        stopin = True
        while stopin:
            num = ''.join(random.choices(string.digits,k=10))
            bot.send_message(message.chat.id, num)
    elif command == '/user':
        bot.send_message(message.chat.id, 'How Many Letters')
        bot.register_next_step_handler(message, user)
    elif command == '/visa':
        numofvisa = 16
        filesave = 'Densor.txt'
        nums = '123456789'
        year = datetime.datetime.now().year
        visa = ''.join((densor(nums) for x in range(numofvisa)))
        visacr = 2023 
        visacvcn = '123456789'
        visacvch = 3
        visacvc = ''.join((densor(visacvcn) for d in range(visacvch)))
        bot.send_message(message.chat.id, f'Visa: {visa} | Year: {visacr} | CVV: {visacvc}')

    elif command == "/password":
        bot.send_message(message.chat.id, 'How Many Letters?')
        bot.register_next_step_handler(message, password)
    elif command == '/stop':
        stopin = False
        bot.send_message(message.chat.id, 'Done. Type /start to begin again')
    else:
        bot.send_message(message.chat.id, 'ERROR')

def user(message):
    try:
        userI = int(message.text)
        global stopin
        stopin = True
        while stopin:
            name = ''.join(random.choices(string.ascii_uppercase, k=userI))
            bot.send_message(message.chat.id, name)
    except:
        bot.send_message(message.chat.id, 'Please enter a number.')
def password(message):
    try:
        userI = int(message.text)
        global stopin
        stopin = True
        while stopin:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=userI))
            bot.send_message(message.chat.id, password)
    except:
        bot.send_message(message.chat.id, 'Please enter a number.')
bot.polling(none_stop=True)
