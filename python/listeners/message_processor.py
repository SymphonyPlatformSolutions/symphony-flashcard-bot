from sym_api_client_python.processors.sym_message_parser import SymMessageParser


class MessageProcessor:
    def __init__(self, bot_client):
        self.bot_client = bot_client
        self.message_parser = SymMessageParser()

    def process(self, msg):
        msg_text = self.message_parser.get_text(msg)
        template = '<messageML>Hello {}, hope you are doing well!You love BOS right?</messageML>'
        msg_to_send = dict(
            message=template.format(self.message_parser.get_im_first_name(msg))
        )

        if msg_text:
            stream_id = self.message_parser.get_stream_id(msg)
            self.bot_client.get_message_client(). \
                send_msg(stream_id, msg_to_send)
