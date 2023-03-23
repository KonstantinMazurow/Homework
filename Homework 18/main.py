import logging
from aiogram import executor
from globals import dp
from handlers import user

logging.basicConfig(level=logging.INFO)
user.register_client_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
