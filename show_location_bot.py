# -*- coding: utf-8 -*-

# config file
import config
# pyTelegramBotAPI - library
import telebot
#
from maps_coordinates import get_coordinates, get_formatted_address


# creating our bot
bot = telebot.TeleBot(config.token)


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
