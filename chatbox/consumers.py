import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatRoom, ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "general_chat"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        user = self.scope["user"]

        if user.is_authenticated:
            await self.save_message(user, message)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "username": user.username,
                }
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def save_message(self, user, message):
        room, created = ChatRoom.objects.get_or_create(name="General")
        ChatMessage.objects.create(room=room, user=user, message=message)