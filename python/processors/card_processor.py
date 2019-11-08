import utils
from utils import log
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
            'Latest NAV',
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
            'Complex Product',
            'Extra Remarks'
        ]

    def send_card(self, stream_id, data_row):
        if type(data_row).__name__ == 'DataFrame':
            data_row = data_row.iloc[0]

        data_row = data_row[self.card_fields]
        data_row.fillna("N/A", inplace = True)
        data_json = '{ "fund": ' + data_row.to_json() + '}'
        log(f'Sent flashcard to {stream_id}')
        log(data_json)
        utils.send_message(stream_id, utils.card_template, data_json)
