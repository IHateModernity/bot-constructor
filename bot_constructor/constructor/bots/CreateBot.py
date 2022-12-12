import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'bot_constructor/constructor/bots/'))


class CreateBot:

    def __read_exemple_file(self):

        with open('constructor/bots/exemple_bot_script.txt', 'r', encoding='utf8') as f:
            return f.readlines()

    def __writefile(self, path_out_file: str, requests_for_bot: list[dict]):
        text_from_exemple = self.__read_exemple_file()

        with open(path_out_file, 'w', encoding='utf8') as f:
            text_from_exemple[3] = 'requests = ' + str(requests_for_bot)

            f.write(''.join(text_from_exemple))

    def __init__(self, path_out_file: str, requests_for_bot: list[dict]):
        if type(path_out_file) != str:
            raise "path_out_file is not str"

        if type(requests_for_bot) != list:
            raise "requests_for_bot is not str"

        self.__writefile(path_out_file, requests_for_bot)
