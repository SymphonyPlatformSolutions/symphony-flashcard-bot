from utils import log
import logging
import traceback
from sym_api_client_python.clients.sym_bot_client import SymBotClient
from sym_api_client_python.listeners.room_listener import RoomListener
from processors.message_processor import MessageProcessor


class RoomListenerImpl(RoomListener):
    def __init__(self, sym_bot_client: SymBotClient):
        self.bot_client = sym_bot_client
        self.msg_processor = MessageProcessor(self.bot_client)

    def on_room_msg(self, msg):
        log('room msg received', msg)
        try:
            self.msg_processor.processROOM(msg)
        except Exception as error:
            traceback.print_exc()
            logging.error(error)

    def on_room_created(self, room_created):
        log('room created', room_created)

    def on_room_deactivated(self, room_deactivated):
        log('room Deactivated', room_deactivated)

    def on_room_member_demoted_from_owner(self, room_member_demoted_from_owner):
        log('room member demoted from owner', room_member_demoted_from_owner)

    def on_room_member_promoted_to_owner(self, room_member_promoted_to_owner):
        log('room member promoted to owner', room_member_promoted_to_owner)

    def on_room_reactivated(self, room_reactivated):
        log('room reactivated', room_reactivated)

    def on_room_updated(self, room_updated):
        log('room updated', room_updated)

    def on_user_joined_room(self, user_joined_room):
        log('USER JOINED ROOM', user_joined_room)

    def on_user_left_room(self, user_left_room):
        log('USER LEFT ROOM', user_left_room)
