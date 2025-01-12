from django.db import models
from django.contrib.auth.models import User
from .managers import UnreadMessagesManager

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # Track if a message has been edited
    edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)  # Timestamp of the last edit
    edited_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="edited_messages"
    )  # User who edited the message

    # Indicates whether the message has been read
    read = models.BooleanField(default=False)

    # Add the custom manager for unread messages
    objects = models.Manager()  # Default manager
    unread = UnreadMessagesManager()  # Custom manager

    parent_message = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )  # Self-referential field for threaded replies

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"

class MessageHistory(models.Model):
    """
    Model to store the history of edited messages.
    """
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="history")
    old_content = models.TextField()  # Previous content of the message
    edited_at = models.DateTimeField(auto_now_add=True)  # When the edit occurred
    edited_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )  # Who made the edit

    def __str__(self):
        def __str__(self):
        return f"Message from {self.sender} to {self.receiver} ({'Read' if self.read else 'Unread'})"


    def get_all_replies(self):
        """
        Recursively fetch all replies to this message.
        """
        replies = list(self.replies.all())
        for reply in self.replies.all():
            replies.extend(reply.get_all_replies())
        return replies


    