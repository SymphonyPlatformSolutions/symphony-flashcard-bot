import logging
import settings
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.processors.sym_message_parser import SymMessageParser


class CardProcessor:
    def __init__(self, bot_client: SymBotClient):
        self.bot_client = bot_client

    def send_message(self, stream_id, msg_text, data_payload):
        message_payload = dict(message=f'<messageML>{msg_text}</messageML>', data=data_payload)
        self.bot_client.get_message_client().send_msg(stream_id, message_payload)
        self.bot_client.get_message_client().send_msg

    def send_card(self, stream_id, data_json):
        data_json = '{ "fund": ' + data_json + '}'
        self.send_message(stream_id, settings.card_template, data_json)
