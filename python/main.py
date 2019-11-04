import utils
from utils import log
from sym_api_client_python.configure.configure import SymConfig
from sym_api_client_python.auth.rsa_auth import SymBotRSAAuth
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from listeners.im_listener_impl import IMListenerImpl
from listeners.room_listener_impl import RoomListenerImpl
import pandas as pd


def main():
    # Configure logging
    utils.configure_logging()
    log('Starting MI Flashcard Bot..')

    # Load bot config
    config = SymConfig('resources/config.json')
    config.load_config()

    # Load data file
    data_file_path = 'python/data.csv'
    if 'dataFilePath' in config.data and len(config.data['dataFilePath']) > 3:
        data_file_path = config.data['dataFilePath']
    log(f'Loading data file from {data_file_path}')
    utils.data = pd.read_csv(data_file_path)
    utils.user_state = {}

    # Load card template
    with open('resources/card-template.ftl', 'r') as file:
        utils.card_template = file.read().replace('\n', '')

    # Authenticate and initialise bot
    auth = SymBotRSAAuth(config)
    auth.authenticate()
    bot_client = SymBotClient(auth, config)

    # Determine admin room stream id
    config_admin_room_name = config.data['adminRoomName']
    room_search = bot_client.get_stream_client().search_rooms(config_admin_room_name, 0, 1)
    if ('rooms' in room_search and len(room_search['rooms']) == 1):
        room = room_search['rooms'][0]
        admin_room_name = room['roomAttributes']['name']
        admin_stream_id = room['roomSystemInfo']['id']
        utils.admin_stream_id = admin_stream_id
        log(f'Located admin room named [{admin_room_name}] at [{admin_stream_id}]')
    else:
        log(f'Cannot locate admin room named {config_admin_room_name}')

    # Set up datafeed service and listeners
    datafeed_event_service = bot_client.get_datafeed_event_service()
    datafeed_event_service.add_im_listener(IMListenerImpl(bot_client))
    datafeed_event_service.add_room_listener(RoomListenerImpl(bot_client))

    # Create and read the datafeed
    log('Starting datafeed')
    datafeed_event_service.start_datafeed()


if __name__ == "__main__":
    main()
