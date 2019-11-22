import re
import base64
import utils
from utils import log
from collections import Counter
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
        self.help_message = 'Welcome to MI Flash Bot. Please use the following commands:<ul><li><b>/help</b>: show this message</li><li><b>/fundname [search query]</b>: search for funds by name</li><li><b>/isin [search query]</b>: search for funds by ISIN</li></ul>'
        self.help_message_admin = 'Welcome to MI Flash Bot. Please use the following commands:<ul><li><b>/help</b>: show this message</li><li><b>/download</b>: get the active data file</li><li><b>/upload</b>: used together with an attached data file to replace the active data file</li><li><b>/blast [message]</b>: used together with an attached file containing 1 email address per line to blast IM messages</li><li><b>/logs</b>: get the bot activity log</li></ul>'

    def parse_message(self, msg):
        stream_id = self.message_parser.get_stream_id(msg)
        msg_text = self.message_parser.get_text(msg)
        command = msg_text[0].lower() if len(msg_text) > 0 else ''
        rest_of_message = str.join(' ', msg_text[1:]) if len(msg_text) > 1 else ''
        return stream_id, msg_text, command, rest_of_message

    def get_attachment(self, stream_id, message_id, file_id):
        attachment = self.message_client.get_msg_attachment(stream_id, message_id, file_id)
        return base64.b64decode(attachment)

    def processROOM(self, msg):
        displayName = msg['user']['displayName']
        stream_id, msg_text, command, rest_of_message = self.parse_message(msg)

        if stream_id != utils.admin_stream_id:
            log(f'Ignoring room message from non-admin stream {stream_id}')
            return

        log(f'Executing admin {command} query from {displayName}')

        if command == '/help':
            utils.send_message(stream_id, self.help_message_admin)

        elif command == '/upload':
            if 'attachments' not in msg or len(msg['attachments']) != 1:
                utils.send_message(stream_id, 'Please attach data file along with /upload')
                return
            self.admin_processor.send_data_file(stream_id)
            attachment = self.get_attachment(stream_id, msg['messageId'], msg['attachments'][0]['id'])
            self.admin_processor.replace_data_file(stream_id, attachment)

        elif command == '/download':
            self.admin_processor.send_data_file(stream_id)

        elif command == '/logs':
            self.admin_processor.send_log_file(stream_id)

        elif command == '/blast':
            if len(msg_text) < 2:
                utils.send_message(stream_id, 'Please use /blast [message]')
                return
            if 'attachments' not in msg or len(msg['attachments']) != 1:
                utils.send_message(stream_id, 'Please attach 1 file containing an email per line along with /blast')
                return
            log(f'Sending blast message: {rest_of_message}')
            attachment = self.get_attachment(stream_id, msg['messageId'], msg['attachments'][0]['id'])
            successful_recipients = self.admin_processor.blast_messages(attachment, rest_of_message)
            utils.send_message(stream_id, f'Blast to {successful_recipients} recipients complete')
            log(f'Blast to {successful_recipients} recipients complete')

        elif command.startswith('/'):
            utils.send_message(stream_id, f'Sorry, I do not understand the command {command}')

    def processIM(self, msg):
        userId = msg['user']['userId']
        displayName = msg['user']['displayName']
        stream_id, msg_text, command, rest_of_message = self.parse_message(msg)

        # Administrative commands
        if command == '/help':
            utils.send_message(stream_id, self.help_message)

        elif command == '/clear':
            utils.send_message(stream_id, '<br/>' * 50)

        # User performs an initial command search
        elif (command == '/isin' or command == '/fundname') and len(rest_of_message) > 0:
            log(f'Executing {command} query from {displayName} against {rest_of_message}')

            if command == '/fundname':
                data_field = 'Funds'
                field_label = 'fund names'
            else:
                data_field = 'ISIN (base ccy)'
                field_label = 'ISIN codes'

            data_rows = self.doSearch(utils.data, rest_of_message, data_field)

            if len(data_rows) == 0:
                utils.send_message(stream_id, f'No results found for {field_label} matching {rest_of_message}')
            elif len(data_rows) == 1:
                self.card_processor.send_card(stream_id, data_rows)
            else:
                self.showMultiOptions(userId, stream_id, data_rows, rest_of_message)
            utils.user_log(msg['user'], command, rest_of_message)

        # User performs a multiple-choice selection
        elif command.isdigit() and userId in utils.user_state.keys():
            choice = int(command) - 1
            if choice <= len(utils.user_state[userId]):
                choice_text = utils.user_state[userId][choice]
                data_row = utils.data[utils.data.Funds == choice_text]
                self.card_processor.send_card(stream_id, data_row)
                del utils.user_state[userId]
            else:
                utils.send_message(stream_id, 'Invalid choice')
            utils.user_log(msg['user'], '/fundname select', choice_text)

        # User does anything else
        else:
            utils.send_message(stream_id, 'Please use /fundname [fund name] or /isin [ISIN]')

    def doSearch(self, data_rows, rest_of_message, data_field):
        search_tokens = set(rest_of_message.lower().split())

        # Partial/full-text search
        if len(search_tokens) == 1:
            return utils.data[utils.data[data_field].str.contains(rest_of_message, flags=re.IGNORECASE, na=False)]

        # Token search
        for i in data_rows.index:
            # Count distinct matching tokens between the search query and data values
            value_tokens = set(str(data_rows.loc[i, 'Funds']).lower().split())
            match_dict = { k: dict(Counter(value_tokens)).get(k, 0) for k in search_tokens }
            sort_weight = sum(match_dict.values())
            data_rows.loc[i, 'sort_weight'] = sort_weight

        # Remove entries with matches less than the maximum number
        max_matches = data_rows['sort_weight'].max()
        data_rows = data_rows[data_rows.sort_weight == max_matches]

        # Sort by token matches in descending then fund name in ascending
        return data_rows.sort_values(['sort_weight', 'Funds'], ascending=[False, True])

    def showMultiOptions(self, userId, stream_id, data_rows, rest_of_message):
        # Extract funds column, slice first 10 results and save
        results = list(data_rows['Funds'])[:10]
        utils.user_state[userId] = results

        # Format results as list items with indexes and send to user
        results_str = ''.join([f"<li>{i+1}: {result}</li>" for i, result in enumerate(results)])
        utils.send_message(stream_id, f"Please choose one option: <ul>{results_str}</ul>")
