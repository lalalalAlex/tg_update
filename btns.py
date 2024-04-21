from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text="Играть", callback_data="play")
    btn2 = InlineKeyboardButton(text="Создатели", callback_data="creators")
    keyboard.add(btn1, btn2)
    return keyboard


def creators():
    keyboard = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton(text='Альберт', url='https://t.me/xD_DxD_Dx')
    btn2 = InlineKeyboardButton(text='Александр', url='https://t.me/Shawnn_ref')
    btn3 = InlineKeyboardButton(text='Ахрор', url='https://t.me/a21101001')
    back = InlineKeyboardButton(text="Назад", callback_data="back")
    keyboard.add(btn1, btn2, btn3, back)
    return keyboard


def characters():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="Слава", callback_data="slava")
    btn2 = InlineKeyboardButton(text="Анжела", callback_data="angela")
    keyboard.add(btn1, btn2)
    return keyboard


def choice():
    keyboard = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    btn1 = KeyboardButton(text="Дальше")
    btn2 = KeyboardButton(text="Назад")
    keyboard.add(btn1, btn2)
    return keyboard


def variant():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="Вариант 1", callback_data="var1")
    btn2 = InlineKeyboardButton(text='Вариант 2', callback_data='var2')
    keyboard.add(btn1, btn2)
    return keyboard


def variant1():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="Вариант 1", callback_data="var3")
    btn2 = InlineKeyboardButton(text='Вариант 2', callback_data='var4')
    keyboard.add(btn1, btn2)
    return keyboard


def back_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='В главное меню', callback_data='main')
    keyboard.add(btn1)
    return keyboard
