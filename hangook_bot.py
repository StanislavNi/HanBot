import config
import telebot
from googletrans import Translator


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['tokorean'])
def input_messages(message):
    sent = bot.send_message(message.chat.id, 'Введите текст')
    bot.register_next_step_handler(sent, translate_to_korean)

def translate_to_korean(message):
    translator = Translator()
    translations = translator.translate([message.text], dest='ko')
    for translation in translations:
        bot.send_message(message.chat.id, translation.text)

@bot.message_handler(commands=['fromkorean'])
def input_messages1(message):
    sent = bot.send_message(message.chat.id, 'Введите текст')
    bot.register_next_step_handler(sent, translate_from_korean)

def translate_from_korean(message):
    translator = Translator()
    translations = translator.translate([message.text], dest='ru')
    for translation in translations:
        bot.send_message(message.chat.id, translation.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
