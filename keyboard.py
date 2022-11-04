from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import logging

menukun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="Andijonbugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="Andijonertaga")
        ],
    ],
)
menufar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="farbugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="farertaga")
        ],
    ],
)
menubux = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="buxbugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="buxertaga")
        ],
    ],
)
menujiz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="jizbugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="jizertaga")
        ],
    ],
)
menunam = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="nambugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="namertaga")
        ],
    ],
)
menunav = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="navoibugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="navoiertaga")
        ],
    ],
)
menuqar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="qarshibugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="qarshiertaga")
        ],
    ],
)
menusam = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="sambugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="samertaga")
        ],
    ],
)
menusur = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="surbugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="surertaga")
        ],
    ],
)
menutosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bugun",callback_data="toshbugun"),
            InlineKeyboardButton(text="Ertaga",callback_data="toshertaga")
        ],
    ],
)




menushahar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Andijon"),
            KeyboardButton(text="Buxoro"),
            KeyboardButton(text="Farg`ona"),
            KeyboardButton(text="Jizzax"),
            KeyboardButton(text="Xorazm"),
            KeyboardButton(text="Namangan"),
            ],
            [

                    KeyboardButton(text="Navoiy"),
                    KeyboardButton(text="Qarshi"),
                    KeyboardButton(text="Samarqand"),
                    KeyboardButton(text="Sirdaryo"),
                    KeyboardButton(text="Surxondaryo"),
                    KeyboardButton(text="Toshkent")
                    ],
        [
                    KeyboardButton(text="Xadis")
        ]
        ],
    resize_keyboard=True
)