import unittest
from bot_constructor.constructor.bots.CreateBot import CreateBot

class GetReq:

    def get_fake_req(self):
        requests = [
            {"token": "1:qqw", "name_bot": "test", "target_type": "command", "target_message": "start",
             "answer": "[test] /start"},

            {"token": "1:qqw", "name_bot": "test", "target_type": "command", "target_message": "help",
             "answer": "[test] /help"},

            {"token": "1:qqw", "name_bot": "test", "target_type": "text", "target_message": "Пинг", "answer": "[test] Понг"}
        ]
        return requests

    def get_real_req(self, token: str):
        requests = [
            {"token": f"{token}", "name_bot": "test", "target_type": "command", "target_message": "start",
             "answer": "[test] /start"},

            {"token": f"{token}", "name_bot": "test", "target_type": "command", "target_message": "help",
             "answer": "[test] /help"},

            {"token": f"{token}", "name_bot": "test", "target_type": "text", "target_message": "Пинг", "answer": "[test] Понг"}
        ]
        return requests


class MyTestCase(unittest.TestCase):

    def test_type_arg(self):
        TypeError_Error = False
        try:
            CreateBot_test = CreateBot(1, 2)
        except TypeError:
            TypeError_Error = True

        self.assertEqual(TypeError_Error, True)

    def test_create_file(self):
        FileNotFoundError_Error = False
        OUTFILE = "TESTmain.py"
        try:
            req = GetReq()
            CreateBot_test = CreateBot(OUTFILE, req.get_real_req(token='5631384218:AAFIuL3pOyWPRFg6NaM70w7o5I-PdQ93gHM'))
            open(OUTFILE)
        except FileNotFoundError:
            FileNotFoundError_Error = True

        self.assertEqual(FileNotFoundError_Error, True)

if __name__ == '__main__':
    unittest.main()
