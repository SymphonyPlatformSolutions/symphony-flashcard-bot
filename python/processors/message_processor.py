import base64
import settings
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.processors.sym_message_parser import SymMessageParser
from .admin_processor import AdminProcessor
from .card_processor import CardProcessor


class MessageProcessor:
    def __init__(self, bot_client: SymBotClient):
        self.bot_client = bot_client
        self.message_client = self.bot_client.get_message_client()
        self.message_parser = SymMessageParser()
        self.admin_processor = AdminProcessor(self.bot_client)
        self.card_processor = CardProcessor(self.bot_client)
        self.help_message = 'Welcome to MI Flash Bot'

    def parse_message(self, msg):
        stream_id = self.message_parser.get_stream_id(msg)
        msg_text = self.message_parser.get_text(msg)
        command = msg_text[0].lower() if len(msg_text) > 0 else ''
        rest_of_message = msg_text[1] if len(msg_text) > 1 else ''
        return stream_id, msg_text, command, rest_of_message

    def get_attachment(self, stream_id, message_id, file_id):
        attachment = self.message_client.get_msg_attachment(stream_id, message_id, file_id)
        return base64.b64decode(attachment)

    def send_message(self, stream_id, msg_text):
        self.message_client.send_msg(stream_id, dict(message=f'<messageML>{msg_text}</messageML>'))

    def processROOM(self, msg):
        stream_id, msg_text, command = self.parse_message(msg)

        if stream_id != settings.admin_stream_id:
            print(f'Ignoring room message from non-admin stream {stream_id}')
            return

        if command == '/help':
            print('doing help')
            self.send_message(stream_id, self.help_message)

        elif command == '/upload':
            print('doing upload')
            self.send_message(stream_id, 'upload')

        elif command == '/download':
            print('doing download')
            self.send_message(stream_id, 'download')

        elif command == '/blast':
            if len(msg_text) < 2:
                self.send_message(stream_id, 'Please use /blast [message]')
                return
            if 'attachments' not in msg or len(msg['attachments']) != 1:
                self.send_message(stream_id, 'Please attach 1 file containing an email per line along with /blast')
                return
            attachment = self.get_attachment(stream_id, msg['messageId'], msg['attachments'][0]['id'])
            self.admin_processor.blast_messages(attachment, str.join(' ', msg_text[1:]))

        elif command.startswith('/'):
            self.send_message(stream_id, f'Sorry, I do not understand the command {command}')

    def processIM(self, msg):
        stream_id, msg_text, command, isin = self.parse_message(msg)

        if command == '/isin' and isin != '':
            print('doing isin')
            data_row = settings.data.loc[[isin.upper()], ['Funds','Factsheet / Offering Material \r\n(via Fundinfo)','Fund Specific Materials \r\n(via Intranet)','Base Ccy','Last Bloomberg Update','1 Mth Return (%)','3 Mths Return (%)','1 Yr Return (%)','3 Yr Ann Return (%)','AR*','Investment Objective','Investment Tenor','Investment Time Horizon','Dealing Frequency (Subscription)\r\n\r\nRefer to Funds Identifier tab for Notice Period','Loss Absorption Product','Complex Product']]
            #data_row = settings.data.loc[[isin.upper()], ['Funds','1 Mth Return (%)','3 Mths Return (%)','1 Yr Return (%)']]
            self.card_processor.send_card(stream_id, data_row)

        elif command == '/fundname':
            print('doing fundname')
            self.send_message(stream_id, 'fundname')

        else:
            self.send_message(stream_id, 'We only support the functions /fundname or /isin')
