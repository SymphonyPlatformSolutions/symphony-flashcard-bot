from sym_api_client_python.listeners.im_listener import IMListener
from .message_processor import MessageProcessor
import logging


class IMListenerImpl(IMListener):
    def __init__(self, sym_bot_client):
        self.bot_client = sym_bot_client
        self.msg_processor = MessageProcessor(self.bot_client)

    def on_im_message(self, im_message):
        logging.debug('message received in IM')
        self.msg_processor.process(im_message)

    def on_im_created(self, im_created):
        logging.debug('IM created!', im_created)
