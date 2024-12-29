from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

# Create the base router for conversations
router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Create a nested router for messages under conversations
nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),           # Include the base routes
    path('', include(nested_router.urls)),    # Include the nested routes
]
