import telebot
from tokens import tele

token = tele


bot = telebot.TeleBot(token, threaded=False)












bot.infinity_polling()