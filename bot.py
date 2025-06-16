import telebot
from telebot import types
from telebot.types import Message, InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb, CallbackQuery as Cq
from db import upd
import tokens

bot = telebot.TeleBot(tokens.token)

data_to_update = []  #template: [id, status] каждый раз делать апдейт данных чтобы общаться с бд to fix:при большой нагрузке возможны фризы
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(True, False)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    markup.add(btn1, btn2)
    id1 = message.chat.id
    print(id1)
    us = f"<b>Hi</b>,<b>{message.from_user.first_name}!</b>\n<b>What you want to do?</b>"
    bot.send_message(message.chat.id, us, parse_mode='html', reply_markup=markup)

#создать функцию для покупки подписки
#   upd(data_to_update)
@bot.message_handler()
def func(message):
    if message.text == "1":
        bot.send_message(message.chat.id, 'тест', parse_mode='html', reply_markup=types.ReplyKeyboardRemove())

    elif message.text == '2':
        bot.send_message(message.chat.id, "test", parse_mode='html', reply_markup=types.ReplyKeyboardRemove())


bot.polling(none_stop=True)
# я
