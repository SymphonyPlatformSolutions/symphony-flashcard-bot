import sys
import logging
import traceback
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from pathlib import Path
from datetime import datetime

def init():
    global bot_client
    global admin_stream_id
    global data_file_path
    global data
    global user_state
    global card_template

def configure_logging():
    mydir = Path('logs')
    mydir.mkdir(exist_ok=True, parents=True)

    logging.basicConfig(
        filename='./logs/mi-bot.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    sys.excepthook = exception_log

    user_log_path = "./logs/user.log"
    user_log_file = Path(user_log_path)
    if not user_log_file.is_file():
        f = open(user_log_path, "x")
        f.write("DateTime,Username,DisplayName,Department,QueryType,QueryString\r\n")
        f.close()

def exception_log(type, value, tb):
    logging.error(str(value))
    f = open('./logs/mi-bot.log', 'a')
    traceback.print_tb(tb, file=f)
    f.close()


def log(message, data = None):
    if data is None:
        print(message)
        logging.info(message)
    else:
        print(message)
        print(data)
        logging.info(message)
        logging.info(data)

def user_log(user, query_type, query_string):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    username = user['username']
    displayName = user['displayName']

    # dept = bot_client.get_user_client().get_user_from_user_name(user.username)
    dept = "N/A"

    f = open("./logs/user.log", "a")
    f.write(f'{dt_string},"{username}","{displayName}","{dept}","{query_type}","{query_string}"\r\n')
    f.close()

def send_message(stream_id, msg_text, data = None, filename = None, attachment = None):
    msg_text = msg_text.replace('&', '&amp;')
    msg_text = f'<messageML>{msg_text}</messageML>'
    message_payload = dict(message=msg_text)

    if filename is not None and attachment is not None:
        bot_client.get_message_client().send_msg_with_attachment(stream_id, msg_text, filename, attachment)
        return

    if data is not None:
        message_payload['data'] = data.replace('&', '&amp;')
    bot_client.get_message_client().send_msg(stream_id, message_payload)
