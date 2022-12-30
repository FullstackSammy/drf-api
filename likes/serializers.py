from rest_framework import serializers
from .models import Like


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like()
        fields = [
            'id', 'owner', 'post', 'created_at',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
