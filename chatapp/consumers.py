import json
from channels.generic.websocket import WebsocketConsumer
from .serializers import MessageSerializer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # Handle received message
        message_data = json.loads(text_data)
        serializer = MessageSerializer(data=message_data)
        if serializer.is_valid():
            serializer.save()
            # Send message to other users
            self.send(text_data=json.dumps(serializer.data))
