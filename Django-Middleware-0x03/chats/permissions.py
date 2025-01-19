from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only participants to view, send, update, or delete messages.
    """

    def has_object_permission(self, request, view, obj):
        # Allow only authenticated users
        if not request.user.is_authenticated:
            return False

        # Check if the user is a participant in the conversation
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()

        # Check if the user is the sender of a message
        if hasattr(obj, 'conversation'):
            return request.user in obj.conversation.participants.all()

        return False
