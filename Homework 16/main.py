import telebot
from telebot import types
from data.config import TOKEN
from pars_joke import get_joke
from data.config import URL_JOKE
from database_joks import Database

db1 = Database('Joks_database.db')
db1.create_table_joks()

bot = telebot.TeleBot(TOKEN)
joke =''

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет 👋")
    markup.add(btn1)
    bot.send_message(message.from_user.id, " Привет! Я бот-генератор шуток! 👋", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global joke
    result = get_joke(URL_JOKE)

    if message.text == 'Привет 👋':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Новая шутка')
        btn2 = types.KeyboardButton('Шутка из избранных')
        btn3 = types.KeyboardButton('Добавить в избранное')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Какую шутку показать❓', reply_markup=markup)

    elif message.text == 'Новая шутка':
        bot.send_message(message.from_user.id, result, parse_mode='Markdown')
        joke = result

    elif message.text == 'Добавить в избранное':
        db1.insert_table_joks([message.from_user.id ,joke])
    
    elif message.text == 'Шутка из избранных':
        try:
            bot.send_message(message.from_user.id, db1.select_random_joks([message.from_user.id]), parse_mode='Markdown')
        except:
            bot.send_message(message.from_user.id, 'У вас нету избранных шуток')

    else:
        bot.send_message(message.from_user.id, 'Please, enter /start')
     
bot.infinity_polling(none_stop=True, interval=0)
