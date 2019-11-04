import logging
from pathlib import Path

def init():
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
