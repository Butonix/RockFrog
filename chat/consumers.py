# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Chat
from django.utils.html import strip_tags

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "chat"

        self.user = self.scope["user"]
        self.username = self.user.username
        print(self.user.username+" connected")

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message = strip_tags(text_data_json['message'])

        if message is not None:
            if message != '':
                chat_message = Chat(user=self.user, message=message)
                chat_message.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.username
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']
        self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
