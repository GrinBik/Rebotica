import telebot, math, os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

keyboard = InlineKeyboardMarkup()
keyboard.row(InlineKeyboardButton("sin", callback_data="sin"),
             InlineKeyboardButton("cos", callback_data="cos"),
             InlineKeyboardButton("tg", callback_data="tg"))

keyboard.row(InlineKeyboardButton("7", callback_data="7"),
             InlineKeyboardButton("8", callback_data="8"),
             InlineKeyboardButton("9", callback_data="9"))

keyboard.row(InlineKeyboardButton("4", callback_data="4"),
             InlineKeyboardButton("5", callback_data="5"),
             InlineKeyboardButton("6", callback_data="6"))

keyboard.row(InlineKeyboardButton("1", callback_data="1"),
             InlineKeyboardButton("2", callback_data="2"),
             InlineKeyboardButton("3", callback_data="3"))

keyboard.row(InlineKeyboardButton("C", callback_data="C"),
             InlineKeyboardButton("0", callback_data="0"),
             InlineKeyboardButton(",", callback_data="."))

value = ""
prev_value = ""

@bot.message_handler(commands = ['start'] )
def get_message(message):
    bot.send_message(message.from_user.id, "0", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.from_user.id, "0", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(query):
    global value, prev_value
    data = query.data

    if data == 'C':
        value = ""
        prev_value = ""
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0',reply_markup=keyboard)
    elif data == '.' and value == '':
        value = '0.'
    elif data == '.':
        if data not in value:
            value += data
    elif data == 'sin':
        if value == '':
            bot.send_message(query.message.chat.id, text="Введите значение угла для вычисления", reply_markup=keyboard)
        else:
            ans = format(math.sin(math.radians(float(value))), '.3f')
            bot.send_message(query.message.chat.id, f"sin ( {value} ) = " + str(ans))
            bot.send_message(query.message.chat.id, "0", reply_markup=keyboard)
            value = ''
            prev_value = ''
    elif data == 'cos':
        if value == '':
            bot.send_message(query.message.chat.id, text="Введите значение угла для вычисления", reply_markup=keyboard)
        else:
            ans = format(math.cos(math.radians(float(value))), '.3f')
            bot.send_message(query.message.chat.id, f"cos ( {value} ) = " + str(ans))
            bot.send_message(query.message.chat.id, "0", reply_markup=keyboard)
            value = ''
            prev_value = ''
    elif data == 'tg':
        if value == '':
            bot.send_message(query.message.chat.id, text="Введите значение угла для вычисления", reply_markup=keyboard)
        else:
            ans = format(math.tan(math.radians(float(value))), '.3f')
            bot.send_message(query.message.chat.id, f"tg ( {value} ) = " + str(ans))
            bot.send_message(query.message.chat.id, "0", reply_markup=keyboard)
            value = ''
            prev_value = ''
    else:
        value += data

    if value != prev_value:
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
        prev_value = value

bot.polling(none_stop=True)
