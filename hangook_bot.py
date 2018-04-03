import config
import telebot
from googletrans import Translator
from telebot import types


bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def translate_all_messages(message):
    translator = Translator()
    translations = translator.translate([message.text], dest='ko')
    for translation in translations:
        bot.send_message(message.chat.id, translation.text)
    markup = types.ReplyKeyboardMarkup()
    markup.row('translate to korean', 'translate from korean')
    markup.row('currency', 'weather')
    bot.send_message(message.chat.id, "Choose the command:",
                     reply_markup=markup)

if __name__ == '__main__':
     bot.polling(none_stop=True)
