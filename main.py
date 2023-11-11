import telebot
from telebot import types
bot = telebot.TeleBot("6452961995:AAEBVnpOGWN8TFm-VLRjpJSuB4ggekdvOCY")

@bot.message_handler(commands=["start"])
def start(message):
    mess = f'Привет {message.from_user.first_name} ученик школы № 40'
    bot.send_message(message.chat.id,mess,parse_mode="html")

@bot.message_handler(commands=["timetable"])
def timetable(message):
    markup = types.InlineKeyboardMarkup()
    btn1=(types.InlineKeyboardButton("5A", callback_data="open5_a"))
    btn2=(types.InlineKeyboardButton("5Б", callback_data="open5_b"))
    btn3=(types.InlineKeyboardButton("5В", callback_data="open5_v"))
    markup.row(btn1,btn2,btn3)
    btn4=(types.InlineKeyboardButton("6A", callback_data="open6_a"))
    btn5=(types.InlineKeyboardButton("6Б", callback_data="open6_b"))
    btn6=(types.InlineKeyboardButton("6В", callback_data="open6_v"))
    markup.row(btn4, btn5, btn6)
    btn7=(types.InlineKeyboardButton("7A", callback_data="open7_a"))
    btn8=(types.InlineKeyboardButton("7Б", callback_data="open7_b"))
    btn9=(types.InlineKeyboardButton("7В", callback_data="open7_v"))
    markup.row(btn7, btn8, btn9)
    btn10=(types.InlineKeyboardButton("8A", callback_data="open8_a"))
    btn11=(types.InlineKeyboardButton("8Б", callback_data="open8_b"))
    btn12=(types.InlineKeyboardButton("8В", callback_data="open8_c"))
    markup.row(btn10, btn11, btn12)
    btn13=(types.InlineKeyboardButton("9A", callback_data="open9_a"))
    btn14=(types.InlineKeyboardButton("9Б", callback_data="open9_b"))
    btn15=(types.InlineKeyboardButton("9В", callback_data="open9_v"))
    markup.row(btn13, btn14, btn15)
    btn16=(types.InlineKeyboardButton("10А", callback_data="open10_a"))
    btn17=(types.InlineKeyboardButton("10Б", callback_data="open10_b"))
    markup.row(btn16, btn17)
    markup.add(types.InlineKeyboardButton("11Б", callback_data="open11"))
    bot.send_message(message.chat.id, 'Ура расписание!', reply_markup=markup)
@bot.callback_query_handler(func=lambda callback : True)
def callback_message(callback):
    if callback.data == 'open5_a':
        photo = open('5а.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open5_b':
        photo = open('5б.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open5_v':
        photo = open('5в.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open6_a':
        photo = open('6а.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open6_b':
        photo = open('6б.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open6_v':
        photo = open('6в.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open7_a':
        photo = open('7а.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open7_b':
        photo = open('7б.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open7_v':
        photo = open('7в.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open8_a':
        photo = open('8а.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open8_b':
        photo = open('8б.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open8_v':
        photo = open('8в.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open9_a':
        photo = open('9a.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open9_b':
        photo = open('9б.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open9_v':
        photo = open('9в.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open10_a':
        photo = open('10а.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open10_b':
        photo = open('10б.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
    elif callback.data == 'open11':
        photo = open('11.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
bot.polling(none_stop=True)

