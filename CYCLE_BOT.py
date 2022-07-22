import telebot
from telebot import types
from Buttons_for_Menu import *
from my_configs import TOKEN_CYCLE_BOT
from products_cycles import products_data


bot = telebot.TeleBot(TOKEN_CYCLE_BOT)


@bot.message_handler(commands=['start'])
def start(message):
    with open('/home/aman/Desktop/TelegramBot/bot1/anim/AnimatedSticker.tgs', 'rb') as animation_file:
        bot.send_animation(message.chat.id, animation_file)
    bot.send_message(
        message.chat.id,
        f'Привет, <b>{message.from_user.first_name}</b>.\
            \nЯ бот <b>{bot.get_me().first_name}.</b>',
        parse_mode='html'
    )
    menu(message)


def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(category_panel)
    button2 = types.KeyboardButton(cycle_panel)
    button3 = types.KeyboardButton(website_panel)
    button4 = types.KeyboardButton(info_panel)
    button5 = types.KeyboardButton(other_panel)
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, f'{menu_panel}', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def panel_buttons(message):

    # Категории
    if message.text == category_panel:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butt1 = types.KeyboardButton(size_panel)
        butt2 = types.KeyboardButton(brand_panel)
        butt3 = types.KeyboardButton(type_panel)
        menu_butt = types.KeyboardButton(menu_panel)
        markup.add(butt1, butt2, butt3, menu_butt)
        bot.send_message(
            message.chat.id, f'{menu_panel} >>> {category_panel}', reply_markup=markup)

    # Велосипеды
    elif message.text == cycle_panel:

        markup = types.InlineKeyboardMarkup()
        button_next = types.InlineKeyboardButton(
            '⬅️ Back', callback_data='Back')
        button_back = types.InlineKeyboardButton(
            'Next ➡️', callback_data='Next')
        markup.add(button_next, button_back)

        bot.send_message(message.chat.id, cycle_panel, reply_markup=markup)

    # Веб-сайт
    elif message.text == website_panel:
        markup_inline = types.InlineKeyboardMarkup(row_width=5)
        butt_inline = types.InlineKeyboardButton(
            'Перейти на сайт', url='https://fullstack-cycle.web.app/')

        markup_inline.add(butt_inline)
        bot.send_message(message.chat.id, website_panel,
                         reply_markup=markup_inline)

    # Другое
    elif message.text == other_panel:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butt_menu = types.KeyboardButton(menu_panel)
        markup.add(butt_menu)
        bot.send_message(message.chat.id, f'{menu_panel} >>> {other_panel}',
                         reply_markup=markup)

    # Информация
    elif message.text == info_panel:
        bot.send_message(
            message.chat.id, f'Меня зовут {bot.get_me().first_name} 🙂\
                \nА тебя зовут {message.from_user.first_name}')
    # Меню
    elif message.text == menu_panel:
        menu(message)

    # Size
    elif message.text == size_panel:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butt1 = types.KeyboardButton(info_in_size)
        menu_butt = types.KeyboardButton(menu_panel)

        markup.add(butt1, menu_butt)
        bot.send_message(message.chat.id, size_panel, reply_markup=markup)

    # Brand
    elif message.text == brand_panel:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu_butt = types.KeyboardButton(menu_panel)

        markup.add(menu_butt)
        bot.send_message(message.chat.id, brand_panel, reply_markup=markup)

    # Type
    elif message.text == type_panel:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu_butt = types.KeyboardButton(menu_panel)

        markup.add(menu_butt)
        bot.send_message(message.chat.id, type_panel, reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Я ничего не нашел 😣')
        menu(message)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'Next':
        for items in products_data['results']:
            mess = f"Title: {items['title']}\
                \nPrice: {items['price']}\
                \nDescription: {items['description']}\
                \nType: {items['category']}\
                \nBarnd: {items['brand']}\
                \nSize: {items['size']}"
            markup = telebot.types.InlineKeyboardMarkup()
            # image_butt = telebot.types.InlineKeyboardButton("Image", url=items['images'][0]['image'])
            # markup.add(image_butt)
            bot.send_message(call.message.chat.id, mess, reply_markup=markup)
        # bot.send_message(call.message.chat.id, 'Тут пока ничего нет 😄')
    elif call.data == 'Back':
        bot.send_message(call.message.chat.id, 'Тут пока ничего нет 😝')


bot.polling(non_stop=True)
