import logging
import settings
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.processors.sym_message_parser import SymMessageParser


class CardProcessor:
    def __init__(self, bot_client: SymBotClient):
        self.bot_client = bot_client
        self.card_fields = [
            'Funds',
            'Factsheet / Offering Material \r\n(via Fundinfo)',
            'Fund Specific Materials \r\n(via Intranet)',
            'Base Ccy',
            'Last Bloomberg Update',
            '1 Mth Return (%)',
            '3 Mths Return (%)',
            '1 Yr Return (%)',
            '3 Yr Ann Return (%)',
            'AR*',
            'Investment Objective',
            'Investment Tenor',
            'Investment Time Horizon',
            'Dealing Frequency (Subscription)\r\n\r\nRefer to Funds Identifier tab for Notice Period',
            'Loss Absorption Product',
            'Complex Product'
        ]

    def send_message(self, stream_id, msg_text, data_payload):
        message_payload = dict(message=f'<messageML>{msg_text}</messageML>', data=data_payload)
        self.bot_client.get_message_client().send_msg(stream_id, message_payload)
        self.bot_client.get_message_client().send_msg

    def send_card(self, stream_id, data_row):
        if type(data_row).__name__ == 'DataFrame':
            data_row = data_row.iloc[0]
        data_row = data_row[self.card_fields]
        data_json = '{ "fund": ' + data_row.to_json() + '}'
        self.send_message(stream_id, settings.card_template, data_json)
