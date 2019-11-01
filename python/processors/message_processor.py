import re
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
        rest_of_message = str.join(' ', msg_text[1:]) if len(msg_text) > 1 else ''
        return stream_id, msg_text, command, rest_of_message

    def get_attachment(self, stream_id, message_id, file_id):
        attachment = self.message_client.get_msg_attachment(stream_id, message_id, file_id)
        return base64.b64decode(attachment)

    def send_message(self, stream_id, msg_text):
        msg_text = msg_text.replace('&', '&amp;')
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
        userId = msg['user']['userId']
        stream_id, msg_text, command, rest_of_message = self.parse_message(msg)

        # User performs an initial command search
        if command == '/isin' or command == '/fundname':
            print(f'Executing {command} query from {userId} against {rest_of_message}')

            if command == '/fundname':
                data_field = 'Funds'
                field_label = 'fund names'
            else:
                data_field = 'ISIN (base ccy)'
                field_label = 'ISIN codes'

            data_rows = settings.data[settings.data[data_field].str.contains(rest_of_message, flags=re.IGNORECASE, na=False)]

            if len(data_rows) == 0:
                self.send_message(stream_id, f'No results found for {field_label} matching {rest_of_message}')
            elif len(data_rows) == 1:
                self.card_processor.send_card(stream_id, data_rows)
            else:
                self.showMultiOptions(userId, stream_id, data_rows)

        # User performs a multiple-choice selection
        elif command.isdigit() and userId in settings.user_state.keys():
            choice = int(command) - 1
            if choice <= len(settings.user_state[userId]):
                choice_text = settings.user_state[userId][choice]
                data_row = settings.data[settings.data['Funds'].str.contains(choice_text, na=False)]
                self.card_processor.send_card(stream_id, data_row)
                del settings.user_state[userId]
            else:
                self.send_message(stream_id, 'Invalid choice')

        # User does anything else
        else:
            self.send_message(stream_id, 'Please use /fundname [fund name] or /isin [ISIN]')

    def showMultiOptions(self, userId, stream_id, data_rows):
        # slice first 10 results and save
        results = list(data_rows['Funds'])[:10]
        settings.user_state[userId] = results

        # format results as list items with indexes and send to user
        results_str = ''.join([f"<li>{i+1}: {result}</li>" for i, result in enumerate(results)])
        self.send_message(stream_id, f"Please choose one option: <ul>{results_str}</ul>")
