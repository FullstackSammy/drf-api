from rest_framework import serializers
from .models import PrivateMessage


class PrivateMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the PrivateMessage model.
    """
    sender = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = PrivateMessage
        fields = (
            'id', 'sender', 'recipient', 'created_at', 'updated_at', 'content')
