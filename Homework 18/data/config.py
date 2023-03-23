from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values(".env")

API_TOKEN = config['API_TOKEN']
RECEPT_API = config['RECEPT_API']
