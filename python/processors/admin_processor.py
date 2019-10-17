import logging
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.processors.sym_message_parser import SymMessageParser


class AdminProcessor:
    def __init__(self, bot_client: SymBotClient):
        self.bot_client = bot_client

    def send_message(self, stream_id, msg_text):
        self.bot_client.get_message_client().send_msg(stream_id, dict(message=f'<messageML>{msg_text}</messageML>'))

    def blast_messages(self, file, message):
        emails = file.splitlines()
        for email in emails:
            user = self.bot_client.get_user_client().get_user_from_email(email, True)
            if len(user) == 0:
                print(f'Cannot find user with email {email}')
                continue
            user_id = user['id']
            stream_id = self.bot_client.get_stream_client().create_im([ user_id ])['id']
            self.send_message(stream_id, f'[Broadcast Message] {message}')
