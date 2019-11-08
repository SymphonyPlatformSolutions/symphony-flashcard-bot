import logging
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from pathlib import Path

def init():
    global bot_client
    global admin_stream_id
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

def log(message, data = None):
    if data is None:
        print(message)
        logging.info(message)
    else:
        print(message)
        print(data)
        logging.info(message)
        logging.info(data)

def send_message(stream_id, msg_text, data_payload = None, attachment = None):
    msg_text = msg_text.replace('&', '&amp;')
    message_payload = dict(message=f'<messageML>{msg_text}</messageML>')

    if data_payload is not None:
        message_payload['data'] = data_payload.replace('&', '&amp;')
    if attachment is not None:
        None

    bot_client.get_message_client().send_msg(stream_id, message_payload)
