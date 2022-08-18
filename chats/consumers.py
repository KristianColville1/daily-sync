import json
from channels.generic.websocket import WebsocketConsumer


class ChatsConsumer(WebsocketConsumer):
    """
    ChatsConsumer class
    """

    def connect(self):
        """
        connecting clients
        """

        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are connected!'
        }))

    def receive(self, text_data):
        """
        recieves messages
        """
        text_json = json.loads(text_data)
        message = text_json['message']
        print('Message: ', message)
