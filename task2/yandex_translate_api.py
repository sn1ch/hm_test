import requests
from pprint import pprint

# API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
# код ответ '{"code":404,"message":"Maximum daily translated text volume exceeded"}'
API_KEY = 'trnsl.1.1.20190511T180824Z.c92969a2f8aa0201.0b7285baa81111777e43e55c9b41c65eae007c1d'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, from_lang, to_lang='ru'):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang)
    }

    response = requests.get(URL, params=params)
    json = response.json()

    # print(json['text'][0])
    # print(response)
    # pprint(response.text)
    # pprint(response.reason)
    # pprint(response.text)
    return response.text


# print(translate_it('suck my dick', 'en'))
# a = 'a'*11000
# print(translate_it(a, 'en'))
