from utils import log
import utils
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.processors.sym_message_parser import SymMessageParser
import pandas as pd


class AdminProcessor:
    def __init__(self, bot_client: SymBotClient):
        self.bot_client = bot_client

    def blast_messages(self, file, message):
        successful_recipients = 0
        emails = file.splitlines()
        for email in emails:
            user = self.bot_client.get_user_client().get_user_from_email(email, True)
            if len(user) == 0:
                log(f'Cannot find user with email {email}')
                continue
            user_id = user['id']
            stream_id = self.bot_client.get_stream_client().create_im([ user_id ])['id']
            utils.send_message(stream_id, f'[Broadcast Message] {message}')
            successful_recipients += 1
        return successful_recipients

    def send_log_file(self, stream_id):
        utils.send_message(stream_id, "The log file is attached", None, "mi-bot.txt", "logs/mi-bot.log")
        None

    def send_data_file(self, stream_id):
        utils.send_message(stream_id, "The current data file is attached", None, "data.csv", utils.data_file_path)
        None

    def replace_data_file(self, stream_id, file):
        log('Writing new data file')
        f = open(utils.data_file_path, 'wb')
        f.write(file)
        f.close()

        log(f'Loading data file from {utils.data_file_path}')
        utils.data = pd.read_csv(utils.data_file_path)
        utils.user_state = {}
        utils.send_message(stream_id, "The current data file has been replaced")
