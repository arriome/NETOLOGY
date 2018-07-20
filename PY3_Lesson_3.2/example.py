import requests
import os

def translate_it(text):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': 'ru-en',
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

a = translate_it('Привет')
print(a)
#dir = os.path.dirname(path)
dir = os.path.abspath('.')
print('Введите язык: 1 - немецкий, 2 - испанский, 3 - французский')
a = int(input())
if a == 1:  
  file = os.path.join(dir, 'ES.txt')
  print('Испанский')
if a == 2:
  file = os.path.join(dir, 'FR.txt')
  print('Французский')
if a == 3:
  file = os.path.join(dir, 'DE.txt')
  print('Немецкий')
  
if os.path.exists(file):
  with open(file) as f:
    text = f.read()
    t = translate_it(text)
    t.write_file('output')
    print(t.get_result())
    f.close()

#with open("index.html","w",encoding="utf-8") as f:
  #f.write(response.text)

# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))


