import config
import telebot
from googletrans import Translator
from telebot import types


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Перевод на корейский', 'Перевод с корейского')
    markup.row('Курс валют', 'Погода')
    bot.send_message(message.chat.id, "Choose the command:",
                     reply_markup=markup)

def commands(message):
    if message.text == 'Перевод на корейский':
        translator = Translator()
        translations = translator.translate([message.text], dest='ko')
        for translation in translations:
            bot.send_message(message.chat.id, translation.text)
    elif message.text == 'Перевод с корейского':
        translator = Translator()
        translations = translator.translate([message.text], dest='ru')
        for translation in translations:
            bot.send_message(message.chat.id, translation.text)

bot.polling()
