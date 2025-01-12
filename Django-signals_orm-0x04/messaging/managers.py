from django.db import models
from django.contrib.auth.models import User

class UnreadMessagesManager(models.Manager):
    """
    Custom manager to filter unread messages for a specific user.
    """
    def unread_for_user(self, user):
        return super().get_queryset().filter(receiver=user, read=False)

