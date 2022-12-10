from typing import Any
import telebot



class HandlerRequests:

    def sorted_target_type(self, all_requests: list) -> tuple[dict[str, str], list[Any], list[Any]]:
        settings = {'token': f'{all_requests[0][0]}'}
        commands = []
        texts = []

        for request in all_requests:
            if request[2] == 'command':
                commands.append(request)
            elif request[2] == 'text':
                texts.append(request)

        return settings, commands, texts

    def converting_command_to_telebot(self, all_command_requests: list) -> list[Any]:
        commands = []
        for command in all_command_requests:
            commands.append(command[3])

        return commands

settings, commands_list, textx_list = HandlerRequests().sorted_target_type(requests)

bot = telebot.TeleBot(settings.get('token'))

@bot.message_handler(commands=HandlerRequests().converting_command_to_telebot(commands_list))
def handler_command(message):
    for command in commands_list:
        if '/' + command[3] == message.text:
            print(command, message.text)
            bot.send_message(message.chat.id, str(command[-1]))


@bot.message_handler(content_types=['text'])
def handler_textx(message):
    for text in textx_list:
        if text[3] == message.text:
            print(text, message.text)
            bot.send_message(message.chat.id, text[-1])

bot.infinity_polling()
