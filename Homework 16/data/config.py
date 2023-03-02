from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

TOKEN = config['TOKEN']


URL_JOKE = 'https://randstuff.ru/joke/'