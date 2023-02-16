from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(read_only=True)
    recipient = serializers.CharField(read_only=True)


    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'message', 'read', 'created_at']
        read_only_fields = ['id', 'read', 'created_at']