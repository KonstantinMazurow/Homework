from aiogram import Dispatcher, types
from utils.parser_recept_food import get_random_recept_food
from states.states import Game
from aiogram.dispatcher import FSMContext
import random


async def send_help(message: types.Message):
    await message.answer("""
        Command List:
        /game - Guess the number game
        /food - Sends a random recipe
    """)


async def send_welcome(message: types.Message):
    await message.answer("""
        Hello. Enter a command. To display a list of commands, type /help
    """)


async def send_random_recept_food(message: types.Message):
    await message.answer(get_random_recept_food())


async def start_message_game(message: types.Message):
    await Game.END.set()
    await message.answer('''
        Welcome to the game "Guess the number". I guessed a number from 0 to 10. You have 3 attempts. Good luck
    ''')
    global num, lives
    num = random.randint(1, 9)
    lives = 3
    await Game.END.set()


async def handle_game_end(message: types.Message, state: FSMContext):
    global num, lives
    answer = message.text
    if answer.isnumeric():
        if lives >= 1:
            if int(answer) == num:
                await message.answer("""
                🎉 Congratulations, you win!!! To play again, type /game
                """)
                await state.finish()
            else:
                lives -= 1
                await message.answer(f"""
                Sorry, think better You have {lives} lives
                """)
                await Game.END.set()
        elif lives == 0:
            await message.answer(f"Sorry, Yoy Loose! Number is {num}. To play again, type /game")
            await state.finish()
    else:
        await message.answer("Sorry, type erorr")
        await Game.END.set()


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_help, commands=['help'])
    dp.register_message_handler(send_random_recept_food, commands=['food'])
    dp.register_message_handler(start_message_game, commands=['game'])
    dp.register_message_handler(handle_game_end, state=Game.END)
