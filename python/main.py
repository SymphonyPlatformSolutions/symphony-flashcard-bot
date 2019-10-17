from pathlib import Path

import logging
from sym_api_client_python.configure.configure import SymConfig
from sym_api_client_python.auth.rsa_auth import SymBotRSAAuth
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from listeners.im_listener_impl import IMListenerImpl
from listeners.room_listener_impl import RoomListenerImpl
import pandas as pd




def configure_logging():
    mydir = Path('logs')
    mydir.mkdir(exist_ok=True, parents=True)

    logging.basicConfig(
        filename='./logs/mi-bot.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filemode='w', level=logging.DEBUG
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def main():
    print('Starting MI Flashcard Bot..')

    # Configure log
    configure_logging()

    fundslist = pd.read_csv('/Users/user/test_bot_amos/python/data.csv')

    # RSA Auth flow: pass path to rsa config.json file
    configure = SymConfig('resources/config.json')
    configure.load_config()
    auth = SymBotRSAAuth(configure)
    auth.authenticate()

    # Initialize SymBotClient with auth and configure objects
    bot_client = SymBotClient(auth, configure)

    # Initialize datafeed service
    datafeed_event_service = bot_client.get_datafeed_event_service()

    # Initialize listener objects and append them to datafeed_event_service
    # Datafeed_event_service polls the datafeed and the event listeners
    # respond to the respective types of events
    datafeed_event_service.add_im_listener(IMListenerImpl(bot_client))
    datafeed_event_service.add_room_listener(RoomListenerImpl(bot_client))

    # Create and read the datafeed
    print('Starting datafeed')
    datafeed_event_service.start_datafeed()


if __name__ == "__main__":
    main()
