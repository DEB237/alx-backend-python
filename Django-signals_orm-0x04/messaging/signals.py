from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Message, Notification, User, MessageHistory

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    instance.sent_messages.all().delete()
    instance.received_messages.all().delete()
    instance.notification_set.all().delete()

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Check if the message already exists
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                # Log the old content in MessageHistory
                MessageHistory.objects.create(
                    message=instance,
                    old_content=old_message.content,
                    edited_by=instance.edited_by
                )
                # Mark the message as edited
                instance.edited = True
                instance.edited_at = instance.edited_at or old_message.timestamp
        except Message.DoesNotExist:
            pass