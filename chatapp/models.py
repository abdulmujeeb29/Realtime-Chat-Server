from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class GroupChat(Chat):
    name = models.CharField(max_length=100)

class GroupChatParticipant(models.Model):
    group_chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)


