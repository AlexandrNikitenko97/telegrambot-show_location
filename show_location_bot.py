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
    answer = config.start_message(message.from_user.first_name, message.from_user.last_name)
    log(message, answer)
    bot.send_message(message.from_user.id, answer)


# if user type /help, help message will shown
@bot.message_handler(commands=['help'])
def command_start(message):
    answer = config.help_message
    log(message, answer)
    bot.send_message(message.from_user.id, answer)


# get 'lat' and 'lng' coordinates and send them via telegram 'find location'
@bot.message_handler(content_types=["text"])
def show_location(message):
    coordinates = get_coordinates(message.text)
    if coordinates is not None:
        answer = "Location sent successfully!"
        log(message, answer)
        bot.send_message(message.from_user.id, "You are looking for: " + get_formatted_address(message.text))
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, latitude=coordinates['lat'], longitude=coordinates['lng'])
    else:
        answer = config.error(message.text)
        log(message, answer)
        bot.send_message(message.from_user.id, answer)


# show log in console
def log(message, answer):
    from datetime import datetime
    print('\n---------------------------------\n')  # for separating log notes
    print(datetime.now())
    print('Message from @{user} - id({id})\nUser text: {text}'.format(
                                                            user=message.from_user.username,
                                                            id=str(message.from_user.id),
                                                            text=message.text))
    print('Bot answer: '+str(answer))

if __name__ == '__main__':
    bot.polling(none_stop=True)
