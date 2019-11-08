from utils import log
import utils
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.processors.sym_message_parser import SymMessageParser


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

    def replace_data_file(self, stream_id):
        utils.send_message(stream_id, "Hello")
        None

    def replace_data_file(self, stream_id, attachment):
        None
