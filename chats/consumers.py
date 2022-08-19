import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatsConsumer(WebsocketConsumer):

    def connect(self):
        """
        Connects users
        """
        self.accept()

    def disconnect(self, close_code):
        """
        Disconnects consumer
        """
        pass

    def receive(self, text_data):
        """
        Receives messages
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

