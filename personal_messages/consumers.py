from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import *
from django.utils.html import strip_tags
from django.core.exceptions import ObjectDoesNotExist
import datetime
from notifications import models as notifications

class PMConsumer(WebsocketConsumer):
    def connect(self):
        user_talking_with_id = self.scope["url_route"]["kwargs"]["user_id"]
        user_talking_with = User.objects.get(pk=user_talking_with_id)
        self.user = self.scope["user"]
        self.conversation_id = get_conversation_and_create_if_not(self.user, user_talking_with).pk
        self.username = self.user.username
        self.room_group_name = "personal_messages_"+str(self.conversation_id)

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
        user = self.user
        user_messaging_with_id = int(strip_tags(text_data_json['user_messaging_with_id']))
        user_messaging_with = None
        try:
            user_messaging_with = User.objects.get(pk=user_messaging_with_id)
        except:
            pass
        if message is not None and message != " ":
            if user.is_authenticated and user_messaging_with is not None:
                # Создаем сообщение и кладём в переписку
                new_conversation_message = ConversationMessage(user=user, text=message, date_time=datetime.datetime.now())
                new_conversation_message.save()
                current_conversation = get_conversation_and_create_if_not(user, user_messaging_with)
                current_conversation.messages.add(new_conversation_message)
                current_conversation.save()
                current_conversation.update_interaction()
                #  Создаём уведомление о сообщении
                notifications.create_notification_on_pm(user, user_messaging_with)
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'pm_message',
                        'message': message,
                        'username': str(new_conversation_message.user.username),
                        'datetime': str(new_conversation_message.date_time.strftime('%d.%m.%Y %H:%M'))
                    }
                )

    def pm_message(self, event):
        message = event['message']
        username = event['username']
        datetime = event['datetime']
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'datetime': datetime
        }))