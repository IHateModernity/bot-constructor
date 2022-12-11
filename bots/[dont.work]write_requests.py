import sqlite3
from typing import Any


class CreateBot:
    # Читаем бд по имени или токену
    def __get_requests_from_one_bot(self, path_db: str, name_bot: str = None, token_bot: str = None) -> list[Any]:
        con = sqlite3.connect(path_db)
        cursor = con.cursor()
        # get_all_info содержит запросы
        if name_bot is not None:
            get_all_info = f"""SELECT token, name_bot, target_type, target_message, answer FROM main WHERE name_bot = '{name_bot}'"""
        else:
            get_all_info = f"""SELECT token, name_bot, target_type, target_message, answer FROM main WHERE token = '{token_bot}'"""

        cursor.execute(get_all_info)
        requests = cursor.fetchall()

        # возвращаем запросы
        return requests

    # Читаем с код и возвращает список содержащий в себе строки с файла
    def __read_exemple_file(self, ) -> list:
        with open('exemple_bot_script.py', 'r', encoding='utf8') as f:
            return f.readlines()


    # outfile - файл в который запишем код, который отправим позже на сайт
    # path_db - путь к базеданных
    # name_bot и token_bot - имя ИЛИ токен бота в бд по которому ищем запросы
    def write_file_answer(self, outfile: str, path_db: str, name_bot='', token_bot=''):
        #открывем файл куда запишем код бота с запросами
        with open(outfile, 'w', encoding='utf8') as f:
            # текст с кодом бота
            text_from_exemple = self.__read_exemple_file()

            # проверяем имя и бота, если пустое кидаем ошибку
            if name_bot is None and token_bot is None:
                raise "bot or token name must not be empty"
            elif name_bot is not None:
                # получаем запросы бота по имени
                requests_for_bot = self.__get_requests_from_one_bot(path_db, name_bot=name_bot)
            else:
                # получаем запросы бота по токену
                requests_for_bot = self.__get_requests_from_one_bot(path_db, token_bot=token_bot)

            # редактируем 4 строку в файле
            text_from_exemple[3] = 'requests = ' + str(requests_for_bot)
            # запись в файл
            f.write(''.join(text_from_exemple))
