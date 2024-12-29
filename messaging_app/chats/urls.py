from rest_framework import routers  # Import routers instead of DefaultRouter directly
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

# Initialize the DefaultRouter using the "routers" prefix
router = routers.DefaultRouter()

# Register the ConversationViewSet
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Create a nested router for messages under conversations
nested_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),           # Include the base routes
    path('', include(nested_router.urls)),    # Include the nested routes
]
