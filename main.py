import telebot
from telebot import types
bot = telebot.TeleBot('6720826974:AAEHr3QOo5klzz-q1sqmKl7mio1j-OM30jI')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет !!!')
@bot.message_handler(commands=['check'])
def start_message(message):
    bot.send_message(message.chat.id,'Python Forever')    
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кликни по мне")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выбирайте ',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кликни по мне":
        bot.send_message(message.chat.id,"https://umschool.net/")
bot.infinity_polling()