from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    user_id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number']


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.
    """
    sender = UserSerializer(read_only=True)
    message_id = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Conversation model with nested messages.
    """
    conversation_id = serializers.CharField(read_only=True)
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']

    def validate(self, data):
        """
        Custom validation to ensure at least two participants in a conversation.
        """
        if 'participants' in data and len(data['participants']) < 2:
            raise serializers.ValidationError("A conversation must have at least two participants.")
        return data
