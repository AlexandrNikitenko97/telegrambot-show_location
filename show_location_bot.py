# -*- coding: utf-8 -*-

# config file
import config
# pyTelegramBotAPI - library
import telebot
# import functions to get json data
from maps_coordinates import get_coordinates, get_formatted_address


# creating our bot
bot = telebot.TeleBot(config.token)


# if user type /start, start message will shown
@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.from_user.id, config.start_message(message.from_user.username))


# if user type /help, help message will shown
@bot.message_handler(commands=['help'])
def command_start(message):
    bot.send_message(message.from_user.id, config.help_message)


# get 'lat' and 'lng' coordinates and send them via telegram 'find location'
@bot.message_handler(content_types=["text"])
def show_location(message):
    coordinates = get_coordinates(message.text)
    if coordinates is not None:
        bot.send_message(message.from_user.id, "You are looking for: " + get_formatted_address(message.text))
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, latitude=coordinates['lat'], longitude=coordinates['lng'])
    else:
        bot.send_message(message.from_user.id, config.error(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)
