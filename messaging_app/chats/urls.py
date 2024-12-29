from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

# Create a DefaultRouter instance
router = DefaultRouter()

# Register the ConversationViewSet
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Register the MessageViewSet
router.register(r'messages', MessageViewSet, basename='message')

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include the DefaultRouter-generated URLs
]
