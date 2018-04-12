import config
import telebot
from telebot import types
from googletrans import Translator
from currency_converter import CurrencyConverter
import pyowm

bot = telebot.TeleBot(config.token)
api_key = 'eab141e5fc97f7e343f8e91ae3a52070'

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('/На_корейский', '/С_корейского')
    markup.row('/Погода', '/Курс')
    bot.send_message(message.chat.id, "Choose the command:",
                     reply_markup=markup)

@bot.message_handler(commands=['На_корейский'])
def input_messages(message):
    sent = bot.send_message(message.chat.id, 'Введите текст')
    bot.register_next_step_handler(sent, translate_to_korean)

def translate_to_korean(message):
    translator = Translator()
    translations = translator.translate([message.text], dest='ko')
    for translation in translations:
        bot.send_message(message.chat.id, translation.text)

@bot.message_handler(commands=['С_корейского'])
def input_messages1(message):
    sent = bot.send_message(message.chat.id, 'Введите текст')
    bot.register_next_step_handler(sent, translate_from_korean)

def translate_from_korean(message):
    translator = Translator()
    translations = translator.translate([message.text], dest='ru')
    for translation in translations:
        bot.send_message(message.chat.id, translation.text)

@bot.message_handler(commands=['Погода'])
def input_message2(message):
    owm = pyowm.OWM('69a45bfc061be421eb86bca86c8c9f36')
    observation = owm.weather_at_place('Seoul,KR')
    w = observation.get_weather()
    weather = str(w) + '\n'\
            + str(str(w.get_temperature('celsius')).split(',')[:-1]) + '\n'\
            + 'Humidity:'+ str(w.get_humidity())+ ' percents'+ '\n'\
            + str(str(w.get_wind()).split(',')[:1])+'m/s'
    weather = weather.split(',',1)[1].replace('status=','Weather status is ')
    weather = weather.replace('temp','Temperature').replace('None','').\
        replace('speed', 'Wind speed ').replace('wind','Wind speed ')
    for char in weather:
        if char in '{}''<>[]""':
            weather = weather.replace(char,'')
    translator = Translator()
    translations = translator.translate([weather], dest='ru')
    for translation in translations:
        bot.send_message(message.chat.id, translation.text)

@bot.message_handler(commands=['Курс'])
def input_message3(message):
    c = CurrencyConverter()
    rate = c.convert(1, 'USD', 'KRW')
    todayrate = ('1 USD = ' + str(rate) + ' KRW')
    bot.send_message(message.chat.id, todayrate)

if __name__ == '__main__':
     bot.polling(none_stop=True)
