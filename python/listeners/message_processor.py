from sym_api_client_python.processors.sym_message_parser import SymMessageParser


class MessageProcessor:
    def __init__(self, bot_client):
        self.bot_client = bot_client
        self.message_client=self.bot_client.get_message_client()
        self.message_parser = SymMessageParser()
        self.help_message='Welcome to MI Flash Bot'

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

    def processIM(self, msg):
        stream_id=self.message_parser.get_stream_id(msg)
        msg_text=self.message_parser.get_text(msg)
        command = msg_text[0]
    
        if command == '/help':
            print('doing help')
            self.send_message(stream_id,self.help_message)

        elif command == '/upload':
            print('doing upload')

            self.send_message(stream_id,'upload')

        elif command == '/download':
            print('doing download')
            self.send_message(stream_id,'download')

        elif command == '/blast':
            print('doing blast')
            self.send_message(stream_id,'blast')

        else:
            self.send_message(stream_id,'Sorry, I do not understand')

    def processROOM(self, msg):
        stream_id = self.message_parser.get_stream_id(msg)
        msg_text = self.message_parser.get_text(msg)
        command = msg_text[0]

        if (command == '/fundname') or (command == '/ISIN'):
            self.send_message(stream_id, self.help_message)

        else: 
            self.send_message(stream_id, 'We only support the functions /FUNDNAME or /ISIN')

    def send_message(self,stream_id,msg_text):
        self.message_client.send_msg(stream_id,dict(message=f'<messageML>{msg_text}</messageML>'))

