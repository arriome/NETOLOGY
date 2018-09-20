
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import os
import chardet  
from os import path
migrations = 'Migrations' 
current_dir = os.path.dirname(os.path.abspath(__file__))
print("DIR:",current_dir)
real_dir = os.path.join(current_dir, migrations)
print("REAL_DIR:", real_dir)
if __name__ == '__main__':
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    cls()                                                           # очищаем экран консоли
    files_word = []
    def find_procedure(real_dir):
        print ("Inside find_proecedure")        
        word = input("INPUT WORDS:")
        files_list = os.listdir(path=real_dir)                      # получаем список всех файлов
        for files in files_list:            
            real_files=os.path.join(real_dir, files) 
            with open(real_files, "rb") as f:                       # получаем кодировку файлов
                text_string = f.read()
                result = chardet.detect(text_string)        
                text_enc = result['encoding']        
            with open(real_files, encoding = text_enc) as sql_file: # ищем слова в списке файлов
                if word in sql_file:                 
                    print("WORD FOUND IN: ",real_files)
                    files_word.append(sql_file)                     # получаем список файлов с вхождениями слов
                    
    while True:
        find_procedure(real_dir)
        out = len(files_word)                                       # считаем количество файлов с вхождениями
        print("FILES COUNT: ",out)

pass    

