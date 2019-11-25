from utils import log
import logging
import traceback
from shutil import copyfile
import utils
import os
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.processors.sym_message_parser import SymMessageParser


class AdminProcessor:
    def __init__(self, bot_client: SymBotClient):
        self.bot_client = bot_client

    def blast_messages(self, file, message):
        successful_recipients = 0
        emails = file.splitlines()
        for email in emails:
            email = email.decode("utf-8").strip()
            if len(email) == 0:
                continue
            user = self.bot_client.get_user_client().get_user_from_email(email, True)
            if len(user) == 0:
                log(f'Cannot find user with email: {email}')
                continue
            try:
                user_id = user['id']
                stream_id = self.bot_client.get_stream_client().create_im([ user_id ])['id']
                utils.send_message(stream_id, f'[Broadcast Message] {message}')
                successful_recipients += 1
            except Exception as error:
                log(f'Cannot send message to user: {email}')
        return successful_recipients

    def send_log_file(self, stream_id):
        utils.send_message(stream_id, "The log file is attached", None, "activity-log.csv", "logs/user.log")
        None

    def send_data_file(self, stream_id):
        utils.send_message(stream_id, "The currently-loaded data file is attached", None, "data.csv", utils.data_file_path)
        None

    def replace_data_file(self, stream_id, file):
        copyfile(utils.data_file_path, utils.data_file_path + '.backup')

        log('Writing new data file')
        f = open(utils.data_file_path, 'wb')
        f.write(file)
        f.close()
