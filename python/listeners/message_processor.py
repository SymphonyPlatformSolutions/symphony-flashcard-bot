from sym_api_client_python.processors.sym_message_parser import SymMessageParser


class MessageProcessor:
    def __init__(self, bot_client):
        self.bot_client = bot_client
        self.message_client = self.bot_client.get_message_client()
        self.message_parser = SymMessageParser()
        self.help_message = 'Welcome to MI Flash Bot'

    def parse_message(self, msg):
        stream_id = self.message_parser.get_stream_id(msg)
        msg_text = self.message_parser.get_text(msg)
        command = msg_text[0].lower()
        return stream_id, msg_text, command

    def send_message(self, stream_id, msg_text):
        self.message_client.send_msg(stream_id, dict(message=f'<messageML>{msg_text}</messageML>'))

    def processROOM(self, msg):
        stream_id, msg_text, command = self.parse_message(msg)

        if command == '/help':
            print('doing help')
            self.send_message(stream_id, self.help_message)

        elif command == '/upload':
            print('doing upload')
            self.send_message(stream_id, 'upload')

        elif command == '/download':
            print('doing download')
            self.send_message(stream_id, 'download')

        elif command == '/blast':
            print('doing blast')
            self.send_message(stream_id, 'blast')

        else:
            self.send_message(stream_id, 'Sorry, I do not understand')

    def processIM(self, msg):
        stream_id, msg_text, command = self.parse_message(msg)

        if command == '/isin':
            print('doing isin')
            self.send_message(stream_id, 'isin')

        elif command == '/fundname':
            print('doing fundname')
            self.send_message(stream_id, 'fundname')

        else:
            self.send_message(stream_id, 'We only support the functions /fundname or /isin')
