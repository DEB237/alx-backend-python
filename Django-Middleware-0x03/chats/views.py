from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipantOfConversation
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer




class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter
