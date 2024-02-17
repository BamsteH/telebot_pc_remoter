import telebot
import os
import webbrowser
import threading
import time

from telebot.apihelper import ApiTelegramException
from telebot import types

def create_keyboard_from_file(file_name):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # read file with utf-8 encoding

    with open(file_name, 'r', encoding='utf-8') as file:

        for line in file:
            buttons = line.split(',')
            buttons[-1] = buttons[-1].replace('\n', '')
            keyboard_buttons = [create_button(name) for name in buttons]
            markup.row(*keyboard_buttons)
    return markup

def create_button(name):
    return types.KeyboardButton(name)

# if file token.txt not exist, create it
if not os.path.exists('token.txt'):
    with open('token.txt', 'w') as file:
        token = input('Enter token of your telegram bot from BotsFather: ')
        file.write(token)
# read token from file in directory
with open('token.txt', 'r') as file:
    token = file.read()
bot = telebot.TeleBot(token)

user_id = None


def get_user_id():
    global user_id
    try:
        with open('user_id.txt', 'r') as file:
            user_id = file.read()
    except FileNotFoundError:
        user_id = None

def rewrite_user_id():
    with open('user_id.txt', 'w') as file:
        global user_id
        user_id = input('Write to bot and chose your id and input here: ')
        file.write(user_id)


def rewrite_token():
    with open('token.txt', 'w') as file:
        token = input('Enter token of your telegram bot from BotsFather: ')
        file.write(token)


def reopen_bot():
    global bot
    with open('token.txt', 'r') as file:
        token = file.read()
    bot = telebot.TeleBot(token)




if __name__ == '__main__':
    print('start')
    while True:
        try:
            @bot.message_handler(commands=['start'])
            def start(message):
                bot.send_message(
                    message.chat.id,
                    'Hello!',
                    reply_markup=create_keyboard_from_file('keyboard.txt')
                )


            @bot.message_handler(content_types=['text'])
            def get_text_messages(message):
                print(str.format('Name: {0}, id: {1}, text: {2}', message.from_user.first_name, message.from_user.id, message.text))
                print(str.format('user_id: {0}', user_id))
                if user_id is None or user_id == '':
                    get_user_id()
                if str(message.from_user.id) == user_id:
                    # message to lower
                    text = str(message.text).lower()
                    print(text)
                    if text == 'turn off computer':
                        os.system('shutdown /s /t 1')
                    if text == 'radio':
                        webbrowser.open('https://www.youtube.com/watch?v=4xDzrJKXOOY')
                        bot.send_message(message.from_user.id, 'Radio is on')
            print('start polling...')

            get_user_id()
            if user_id is None or user_id == '':
                print('Please, write to bot and chose your id')
                thread = threading.Thread(target=rewrite_user_id)
                thread.start()

            print('bot is polling...')
            bot.polling(none_stop=True)

        except ApiTelegramException as e:
            print('Token is not defined, please, enter the valid token')
            rewrite_token()
            reopen_bot()
        except Exception as e:
            print(e)
            time.sleep(5)
            if e.args[0] == 'Bot token is not defined':
                print('Token is not defined, please, enter the valid token')
                rewrite_token()
                reopen_bot()
