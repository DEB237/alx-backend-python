from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} about Message {self.message.id}"

class Message(models.Model):
    ...
    parent_message = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )

    def get_replies(self):
        return self.replies.all()
    
messages = Message.objects.select_related('sender', 'receiver').prefetch_related('replies')
