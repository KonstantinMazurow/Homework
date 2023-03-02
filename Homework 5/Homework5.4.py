from transliterate.base import TranslitLanguagePack, registry
# создаем собстветый перевод с одних букв на другие
class HelloWorldLanguagePack(TranslitLanguagePack):
    language_code = "hw"
    language_name = "HelloWorld"
    mapping = (
       'HeloWrd',
       'ХелоВрд',
    )
# регистрируем его
registry.register(HelloWorldLanguagePack)
# импорт созданного перевода
from transliterate import get_available_language_codes, translit
'hw' in get_available_language_codes()

text = 'Hello World'
print(translit(text, language_code='hw'))