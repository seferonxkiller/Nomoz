from aiogram.types import Message ,CallbackQuery
from aiogram import executor
from aiogram.utils.callback_data import CallbackData
from config import dp,bot
from keyboard import menushahar,menukun,menufar,menubux,menujiz,menunam,menunav,menuqar,menusam,menusur,menutosh
import logging
from datetime import datetime
import json
import requests

# # time_in_utc variable will be the utc time
# time_in_utc = datetime.utcnow()
# # If you want to make it more fancier:
# formatted_time_in_utc = time_in_utc.strftime("%d/%m/%Y %H:%M:%S")



@dp.message_handler(commands='start')
async def start(message: Message):
    text = f"Assalomu Alaykum, {message.from_user.full_name} Nomoz vaqtlari botimizga xush kelibsiz\n" \
           f"Shaharingizni tanlang"
    await message.answer_photo(open("rasm/unnamed.png","rb"),text,reply_markup=menushahar)


@dp.message_handler(commands='help')
async def help(message: Message):
    await message.answer("shu kishiga yozing https://t.me/Dilshodjon404")




@dp.message_handler(text='Andijon')
async def andi(message: Message):
    text = "Kunni tanlang"
    await message.answer(text,reply_markup=menukun)

@dp.callback_query_handler(text='Andijonbugun')
async def bug(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/andijon"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/unnamed2.png", "rb"))
    for prayer in data["today"]:
        await call.message.answer(prayer + ": " + data["today"][prayer])
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='Andijonertaga')
async def erta(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/andijon"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/unnamed1.png", "rb"))
    for prayer in data["tomorrow"]:
        await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
    await call.answer(cache_time=60)

@dp.message_handler(text='Buxoro')
async def andi(message: Message):
    text="Kunni tanlang"
    await message.answer(text,reply_markup=menubux)

@dp.callback_query_handler(text='buxbugun')
async def buxbu(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/buxoro"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/unnamed.png", "rb"))
    for prayer in data["today"]:
        await call.message.answer(prayer + ": " + data["today"][prayer])
        await call.answer(cache_time=60)

@dp.callback_query_handler(text='buxertaga')
async def erta(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/andijon"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/ramtpmkaaba.jpg", "rb"))
    for prayer in data["tomorrow"]:
        await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
    await call.answer(cache_time=60)


@dp.message_handler(text='Farg`ona')
async def andi(message: Message):
    text = "Kunni tanlang"
    await message.answer(text,reply_markup=menufar)

@dp.callback_query_handler(text='farbugun')
async def bug(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/farg'ona"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/ramadan-mubarak-arabic-calligraphy-greeting-600w-1054208462.webp", "rb"))
    for prayer in data["today"]:
        await call.message.answer(prayer + ": " + data["today"][prayer])
        await call.answer(cache_time=60)

@dp.callback_query_handler(text='farertaga')
async def erta(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/farg'ona"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/ramadan-kareem-mubarak-greeting-cards-arabic-calligraphy-style-translation-generous-ramadhan-ramazan-holy-fasting-month-116284221.jpg", "rb"))
    for prayer in data["tomorrow"]:
        await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
        await call.answer(cache_time=60)

# @dp.message_handler(text='Jizzax')
# async def andi(message: Message):
#     text = "Kunni tanlang"
#     await message.answer(text,reply_markup=menujiz)
#
# @dp.callback_query_handler(text='jizbugun')
# async def jizbu(call: CallbackQuery):
#     shahar = 'Jizzax'
#     url = "https://dailyprayer.abdulrcs.repl.co/api/" + shahar
#     response = requests.get(url)
#     data = response.json()
#     await call.message.answer_photo(open("rasm/pngtree-golden-ramadan-mubarak-arabic-text-greeting-with-lantern-png-image_6021813.jpg", "rb"))
#     for prayer in data["today"]:
#         await call.message.answer(prayer + ": " + data["today"][prayer])
# @dp.callback_query_handler(text='jizertaga')
# async def erta(call: CallbackQuery):
#     shahar = 'Jizzax'
#     url = "https://dailyprayer.abdulrcs.repl.co/api/" + shahar
#     response = requests.get(url)
#     data = response.json()
#     await call.message.answer_photo(open("rasm/images444.jpeg", "rb"))
#     for prayer in data["tomorrow"]:
#         await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
#         await call.answer(cache_time=60)
#
# @dp.message_handler(text='Xorazm')
# async def andi(message: Message):
#     shahar = 'Xorazm'
#     url = "https://dailyprayer.abdulrcs.repl.co/api/" + shahar
#     response = requests.get(url)
#     data = response.json()
#     await message.answer(data['city'])
#     await message.answer(data['date'])
#     for prayer in data["today"]:
#         await message.answer(prayer + ": " + data["today"][prayer])


@dp.message_handler(text='Namangan')
async def andi(message: Message):
    text = "Kunni tanlang"
    await message.answer(text,reply_markup=menunam)

@dp.callback_query_handler(text='nambugun')
async def nam(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/namangan"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/images.jpeg", "rb"))
    for prayer in data["today"]:
        await call.message.answer(prayer + ": " + data["today"][prayer])
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='namertaga')
async def erta(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/namangan"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/calligraphie-arabe-pour-ramadan-kareem-71958348.jpg", "rb"))
    for prayer in data["tomorrow"]:
        await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
        await call.answer(cache_time=60)

@dp.message_handler(text='Navoiy')
async def andi(message: Message):
    text = "Kunni tanlang"
    await message.answer(text,reply_markup=menunav)

@dp.callback_query_handler(text='navoibugun')
async def nav(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/navoiy"
    response = requests.get(url)
    data = response.json()
    for prayer in data["today"]:
        await call.message.answer_photo(open("rasm/unnamed2.png", "rb"))
        await call.message.answer(prayer + ": " + data["today"][prayer])
        await call.answer(cache_time=60)

@dp.callback_query_handler(text='navoiertaga')
async def erta(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/navoiy"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/unnamed1.pngn", "rb"))
    for prayer in data["tomorrow"]:
        await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
        await call.answer(cache_time=60)

@dp.message_handler(text='Qarshi')
async def andi(message: Message):
    text = "Kunni tanlang"
    await message.answer(text,reply_markup=menuqar)

@dp.callback_query_handler(text='qarshibugun')
async def qar(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/qarshi"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/unnamed.png", "rb"))
    for prayer in data["today"]:
        await call.message.answer(prayer + ": " + data["today"][prayer])
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='qarshiertaga')
async def erta(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/qarshi"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/ramtpmkaaba.jpg", "rb"))
    for prayer in data["tomorrow"]:
        await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
        await call.answer(cache_time=60)

@dp.message_handler(text='Samarqand')
async def andi(message: Message):
    text = "Kunni tanlang"
    await message.answer(text,reply_markup=menusam)


@dp.callback_query_handler(text='sambugun')
async def sam(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/samarqand"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/ramadan-mubarak-arabic-calligraphy-greeting-600w-1054208462.webp", "rb"))
    for prayer in data["today"]:
        await call.message.answer(prayer + ": " + data["today"][prayer])
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='samertaga')
async def erta(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/samarqand"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/ramadan-kareem-mubarak-greeting-cards-arabic-calligraphy-style-translation-generous-ramadhan-ramazan-holy-fasting-month-116284221.jpg", "rb"))
    for prayer in data["tomorrow"]:
        await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
        await call.answer(cache_time=60)

# @dp.message_handler(text='Sirdaryo')
# async def andi(message: Message):
#     shahar = 'Sirdaryo'
#     url = "https://dailyprayer.abdulrcs.repl.co/api/" + shahar
#     response = requests.get(url)
#     data = response.json()
#     await message.answer(data['city'])
#     await message.answer(data['date'])
#     for prayer in data["today"]:
#         await message.answer(prayer + ": " + data["today"][prayer])


@dp.message_handler(text='Surxondaryo')
async def andi(message: Message):
    text = "Kunni tanlang"
    await message.answer(text,reply_markup=menusur)

@dp.callback_query_handler(text='surbugun')
async def sur(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/denov"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/pngtree-golden-ramadan-mubarak-arabic-text-greeting-with-lantern-png-image_6021813.jpg", "rb"))
    for prayer in data["today"]:
        await call.message.answer(prayer + ": " + data["today"][prayer])
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='surertaga')
async def erta(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/denov"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/images444.jpeg", "rb"))
    for prayer in data["tomorrow"]:
        await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
        await call.answer(cache_time=60)

@dp.message_handler(text='Toshkent')
async def andi(message: Message):
    text = "Kunni tanlang"
    await message.answer(text,reply_markup=menutosh)

@dp.callback_query_handler(text='toshbugun')
async def tosh(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/toshkent"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/images.jpeg", "rb"))
    for prayer in data["today"]:
        await call.message.answer(prayer + ": " + data["today"][prayer])
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='toshertaga')
async def erta(call: CallbackQuery):
    url = "https://dailyprayer.abdulrcs.repl.co/api/toshkent"
    response = requests.get(url)
    data = response.json()
    await call.message.answer_photo(open("rasm/calligraphie-arabe-pour-ramadan-kareem-71958348.jpg","rb"))
    for prayer in data["tomorrow"]:
        await call.message.answer(prayer + ": " + data["tomorrow"][prayer])
        await call.answer(cache_time=60)


@dp.message_handler(text='Xadis')
async def xadis(message: Message):
 text = f"Vobisa ibn Ma’baddan (r.a.)  rivoyat qilinadi.\n" \
        f"Bu zot Rasululloh sollallohu alayhi vasallam huzurlariga kelganlarida, Rasululloh sollallohu alayhi vasallam: «Yaxshilik va gunoh haqida so‘rash uchun keldingmi?» dedilar.\n" \
        f"Shunda bu zot: «Ha», deganlarida, Rasululloh sollallohu alayhi vasallam: «Qalbingdan fatvo so‘ra.\n" \
        f"Yaxshilik -nafs va qalb unga xotirjam bo‘lganidir.\n" \
        f"Gunoh - nafs xira bo‘lib, qalb beqaror bo‘lganidir.\n" \
        f" Agar kishilar senga fatvo berishsa ham va berdirishsa ham», dedilar.\n" \
        f"Imom Ahmad va Doramiylar  rivoyati.\n" \
        f"Navvos ibn Sam’ondan (r.a.)  rivoyat qilinadi.\n" \
        f"Rasululloh sollallohu alayhi vasallam: «Yaxshilik husni xulqdir.\n" \
        f"Yomonlik - nafsing kirlanib, kishilar undan xabardor bo‘lishlarini karih ko‘rganingdir», dedilar.\n" \
        f"Imom Muslim  rivoyatlari."
 await message.answer(text)


if __name__ == '__main__':
    executor.start_polling(dp)
# import time
# from datetime import timezone
# import datetime,calendar
# import pytz
#
# # Getting the current date
# # and time
# dt = datetime.datetime.now(pytz.timezone('Asia/Tashkent'))
#
# utc_time = dt.replace(tzinfo=timezone.utc)
# utc_timestamp = utc_time.timestamp()
#
# print(utc_timestamp)
# print(datetime.datetime.now())
#
# gmt = time.gmtime()
# print("GMT: ",gmt)