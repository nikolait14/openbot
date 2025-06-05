import telebot
from telebot import types

import tokens

bot = telebot.TeleBot(tokens.token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("")
    btn2 = types.KeyboardButton("")
    markup.add(btn1, btn2)
    us = f"<b>Hi</b>,<b>{message.from_user.first_name}</b>"
    bot.send_message(message.chat.id, us, parse_mode='html', reply_markup=markup)


@bot.message_handler()
def func(message):
    if message.text == "":
        bot.send_message(message.chat.id, '<b>ПН-ПТ</b>-7:00-21:00\n<b>СБ-ВС</b>-9:00-19:00', parse_mode='html')
    elif message.text == '':
        bot.send_message(message.chat.id, "test", parse_mode='html')


bot.polling(none_stop=True)
