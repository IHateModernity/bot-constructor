class CreateBot:

    def __read_exemple_file(self):
        with open('exemple_bot_script.py', 'r', encoding='utf8') as f:
            return f.readlines()

    def __writefile(self, path_out_file: str, requests_for_bot: list[dict]):
        text_from_exemple = self.__read_exemple_file()
        with open(path_out_file, 'w', encoding='utf8') as f:
            # редактируем 4 строку в файле
            text_from_exemple[3] = 'requests = ' + str(requests_for_bot)
            # запись в файл
            f.write(''.join(text_from_exemple))

    def __init__(self, path_out_file: str, requests_for_bot: list[dict]):
        self.__writefile(path_out_file, requests_for_bot)

# CreateBot('main.py', requests)
