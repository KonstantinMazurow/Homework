import requests
from data.config import CRYPTO_API


r = requests.get(CRYPTO_API)
data = r.json()
data_parser = data[0:20]


def get_crypto_name():
    crypto_names_values = {}
    for row in data_parser:
        crypto_names_values.update({str(row['name'].lower()):
                                    str(row["quotes"]["USD"]["price"])})
    return crypto_names_values
