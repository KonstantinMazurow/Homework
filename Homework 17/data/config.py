from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

API_TOKEN = config['API_TOKEN']
LINK = config['LINK']
CRYPTO_API = config['CRYPTO_API']
