import config
import telebot
from googletrans import Translator


bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def translate_all_messages(message):
    translator = Translator()
    translations = translator.translate([message.text], dest='ko')
    for translation in translations:
        bot.send_message(message.chat.id, translation.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)