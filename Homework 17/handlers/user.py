from aiogram import Dispatcher, types
from utils.parser import get_pictures
from utils.parser_crypto import get_crypto_name
from state.states import Crypto_Get_Price
from aiogram.dispatcher import FSMContext


async def send_welcome(message: types.Message):
    await message.answer("""Hi!, to display a random picture of a dog, enter /dog, to display information on cryptocurrency, enter the command /crypto.""")


async def send_cat(message: types.Message):
    await message.answer(get_pictures())


async def crypto_message_handler(message: types.Message):
    await Crypto_Get_Price.END.set()
    await message.answer('For which cryptocurrency to export cost information, select from the list or type "exit":')
    for row in get_crypto_name().keys():
        await message.answer(row)
    await Crypto_Get_Price.C1.set()


async def handle_c1_answer(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    if answer in get_crypto_name():
        await message.answer(f'1 {answer} = {get_crypto_name()[answer]} USD 💲')
        await Crypto_Get_Price.C1.set()
    elif answer == "exit":
        await Crypto_Get_Price.END.set()
    else:
        await message.answer("Incorrect value, enter the name of the cryptocurrency from the list.")
        await Crypto_Get_Price.C1.set()


async def handle_end_state(message: types.Message, state: FSMContext):
    await message.answer("Thx, to start the bot, type /start again.")
    await state.finish()


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 's'])
    dp.register_message_handler(send_cat, commands=['dog', 'd'])
    dp.register_message_handler(crypto_message_handler, commands=['crypto'])
    dp.register_message_handler(handle_c1_answer, state=Crypto_Get_Price.C1)
    dp.register_message_handler(handle_end_state, state=Crypto_Get_Price.END)
