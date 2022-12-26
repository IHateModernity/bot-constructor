from typing import Any
import telebot

requests = [{'token': 'token2203', 'name_bot': 'Bot', 'target_message': 'target', 'answer': "Bot's answer"}]

class HandlerRequests:

    def sorted_target_type(self, all_requests: list) -> tuple[dict[str, str], list[Any], list[Any]]:
        settings = {'token': f'{all_requests[0].get("token")}'}
        commands = []
        texts = []

        for request in all_requests:

            if request.get('target_type') == 'command':
                commands.append(request)
            elif request.get('target_type') == 'text':
                texts.append(request)

        return settings, commands, texts

    def converting_command_to_telebot(self, all_command_requests: list) -> list[Any]:
        commands = []
        for command in all_command_requests:
            commands.append(command.get('target_message'))

        return commands


settings, commands_list, textx_list = HandlerRequests().sorted_target_type(requests)
print(textx_list)
bot = telebot.TeleBot(settings.get('token'))


@bot.message_handler(commands=HandlerRequests().converting_command_to_telebot(commands_list))
def handler_command(message):
    for command in commands_list:

        if '/' + command.get('target_message') == message.text:
            bot.send_message(message.chat.id, command.get('answer'))


@bot.message_handler(content_types=['text'])
def handler_textx(message):
    for text in textx_list:
        if text.get('target_message') == message.text:
            bot.send_message(message.chat.id, text.get('answer'))


bot.infinity_polling(none_stop=True)

