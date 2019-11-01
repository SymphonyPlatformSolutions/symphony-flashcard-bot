import logging
import settings
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.processors.sym_message_parser import SymMessageParser


class CardProcessor:
    def __init__(self, bot_client: SymBotClient):
        self.bot_client = bot_client
        self.card_fields = [
            'Funds',
            'Factsheet / Offering Material (via Fundinfo)',
            'Fund Specific Materials (via Intranet)',
            'Base Ccy',
            'Last Bloomberg Update',
            '1 Mth Return (%)',
            '3 Mths Return (%)',
            'YTD Return (%)',
            '1 Yr Return (%)',
            '3 Yr Ann Return (%)',
            'ISIN (base ccy)',
            'Is this a High Yield Bond Fund (Yes/No)',
            'Risk Rating',
            'AR*',
            'Investment Objective',
            'Investment Tenor',
            'Investment Time Horizon',
            'Dealing Frequency (Subscription) Refer to Funds Identifier tab for Notice Period',
            'Loss Absorption Product',
            'Complex Product'
        ]

    def send_message(self, stream_id, msg_text, data_payload):
        data_payload = data_payload.replace('&', '&amp;')
        msg_text = msg_text.replace('&', '&amp;')
        message_payload = dict(message=f'<messageML>{msg_text}</messageML>', data=data_payload)
        self.bot_client.get_message_client().send_msg(stream_id, message_payload)
        self.bot_client.get_message_client().send_msg

    def send_card(self, stream_id, data_row):
        if type(data_row).__name__ == 'DataFrame':
            data_row = data_row.iloc[0]

        data_row = data_row[self.card_fields]
        data_row.fillna("N/A", inplace = True)
        data_json = '{ "fund": ' + data_row.to_json() + '}'

        print(data_json)

        self.send_message(stream_id, settings.card_template, data_json)
