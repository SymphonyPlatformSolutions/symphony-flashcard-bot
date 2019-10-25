import logging
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.processors.sym_message_parser import SymMessageParser


class CardProcessor:
    def __init__(self, bot_client: SymBotClient):
        self.bot_client = bot_client

    def send_message(self, stream_id, msg_text):
        self.bot_client.get_message_client().send_msg(stream_id, dict(message=f'<messageML>{msg_text}</messageML>'))

    def send_card(self, stream_id, data_row):
        # TODO: format card
        self.send_message(stream_id, data_row)
