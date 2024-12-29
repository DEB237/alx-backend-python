from rest_framework import routers  # Import routers instead of DefaultRouter directly
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

# Initialize the DefaultRouter using the "routers" prefix
router = routers.DefaultRouter()

# Register the ConversationViewSet
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Register the MessageViewSet
router.register(r'messages', MessageViewSet, basename='message')

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include the DefaultRouter routes
]
