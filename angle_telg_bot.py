import telebot, math, os
from telebot import types
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)
flag = ''


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("START")
    btn2 = types.KeyboardButton("HELP")
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет! Я бот для вычисления cos, sin и tg угла.\nХотите начать?",
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    global flag
    if (message.text == "HELP"):
        bot.send_message(message.chat.id, text="Нажмите кнопку START ))")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("START")
        btn2 = types.KeyboardButton("HELP")
        keyboard.add(btn1, btn2)
    elif (message.text == "START"):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("cos (косинус)")
        btn2 = types.KeyboardButton("sin (синус)")
        btn3 = types.KeyboardButton("tg (тангенс)")
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        bot.send_message(message.chat.id, text="Выберите что будем вычислять", reply_markup=keyboard)
    elif message.text == 'cos (косинус)':
        flag = 'cos'
        bot.send_message(message.chat.id, text="Введите угол для вычиления cos (косинуса)")
    elif message.text == 'sin (синус)':
        flag = 'sin'
        bot.send_message(message.chat.id, text="Введите угол для вычиления sin (синуса)")
    elif message.text == 'tg (тангенс)':
        flag = 'tg'
        bot.send_message(message.chat.id, text="Введите угол для вычиления tg (тангенса)")
    elif flag != '':
        try:
            angle = int(message.text)
        except:
            bot.send_message(message.chat.id, text="Введите корректное значение угла")
        else:
            if flag == 'sin':
                ans = format(math.sin(math.radians(angle)), '.3f')
                flag = ''
                bot.send_message(message.chat.id, text=f"sin ( {angle} ) = " + str(ans))
            elif flag == 'cos':
                ans = format(math.cos(math.radians(angle)), '.3f')
                flag = ''
                bot.send_message(message.chat.id, text=f"cos ( {angle} ) = " + str(ans))
            elif flag == 'tg':
                ans = format(math.tan(math.radians(angle)), '.3f')
                flag = ''
                bot.send_message(message.chat.id, text=f"tg ( {angle} ) = " + str(ans))
    else:
        bot.send_message(message.chat.id, text='Не торопитесь )) давайте попорядку ;)')

bot.polling(none_stop=True)