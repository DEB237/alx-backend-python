from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, retrieving, and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['participants__username']  # Allow searching by participant username

    @action(detail=False, methods=['post'])
    def create_conversation(self, request):
        """
        Custom action to create a new conversation with participants.
        """
        participants = request.data.get('participants')
        if not participants or len(participants) < 2:
            return Response(
                {"error": "A conversation must have at least two participants."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, retrieving, and creating messages in a conversation.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [SearchFilter]
    search_fields = ['message_body']  # Allow searching by message content

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        """
        Custom action to send a message in an existing conversation.
        """
        conversation = self.get_object()
        sender = request.user
        message_body = request.data.get('message_body')

        if not message_body:
            return Response(
                {"error": "Message body cannot be empty."},
                status=status.HTTP_400_BAD_REQUEST
            )

        message = Message.objects.create(
            conversation=conversation,
            sender=sender,
            message_body=message_body
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
