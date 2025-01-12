from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, User

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    instance.sent_messages.all().delete()
    instance.received_messages.all().delete()
    instance.notification_set.all().delete()
