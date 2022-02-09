import telebot
from telebot import types
import random
bot = telebot.TeleBot("5200162176:AAEEm9siwknp3MGNoOfpiLFtQtxV85vK4A4")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("хочу" , "не хочу")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)
@bot.message_handler(commands=['random'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("хочу число побольше!", "хочу число поменьше!")
    bot.send_message(message.chat.id, 'ваше число: ' + str(random.randint(100, 1000)),reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Мои функции:\n'
                     '/start - Ну что, начнем?\n'
                     '/random - Пора немного отвлечься :)\n'
                     '/help - я тебя всему научу, не переживай')
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "не хочу":
        bot.send_message(message.chat.id, 'Тогда скорее на стрим, боец! https://www.twitch.tv/')
    if message.text.lower() == "хочу число побольше!":
        bot.send_message(message.chat.id, 'ваше число: ' + str(random.randint(1000, 10000)))
    if message.text.lower() == "хочу число поменьше!":
        bot.send_message(message.chat.id, 'ваше число: ' + str(random.randint(0, 100)))
bot.infinity_polling()



