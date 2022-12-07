import sqlite3
from typing import Any


def get_requests_from_one_bot(name_bot: str = None, token_bot: str = None) -> list[Any]:
    if name_bot is None and token_bot is None:
        raise "bot or token name must not be empty"

    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()

    if name_bot is not None:
        get_all_info = f"""SELECT token, name_bot, target_type, target_message, answer FROM main WHERE name_bot = '{name_bot}'"""
    else:
        get_all_info = f"""SELECT token, name_bot, target_type, target_message, answer FROM main WHERE token = '{token_bot}'"""

    cursor.execute(get_all_info)
    info = cursor.fetchall()

    return info


def read_exemple_file() -> list:
    with open('exemple_bot_script.py', 'r', encoding='utf8') as f:
        return f.readlines()

def write_file_answer(name_bot='test') -> str:
    with open('aa.py', 'w', encoding='utf8') as f:
        text_from_exemple = read_exemple_file()
        requests_for_bot = get_requests_from_one_bot(name_bot=name_bot)

        text_from_exemple[3] = 'requests = ' + str(requests_for_bot)

        return ''.join(text_from_exemple)

