from rest_framework import serializers
from .models import ChatMessage, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ChatMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = ChatMessage
        fields = ['sender', 'receiver', 'message', 'timestamp']