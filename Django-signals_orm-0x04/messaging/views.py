from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Message
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

def delete_user(request):
    """
    Deletes the authenticated user's account.
    """
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({"error": "User is not authenticated"}, status=401)

    user.delete()  # Trigger post_delete signal
    return JsonResponse({"message": "User account deleted successfully"}, status=200)

def message_list(request):
    """
    Fetch and display messages sent or received by the authenticated user with optimized queries.
    """
   @method_decorator(cache_page(60), name='dispatch')
def message_list(request):
    """
    Fetch and display messages in a conversation with caching enabled.
    """
    messages = Message.objects.filter(conversation=conversation).select_related('sender', 'receiver')
    return render(request, 'messaging/message_list.html', {'messages': messages})

def message_replies(request, message_id):
    """
    Fetch and display replies to a specific message in a threaded format.
    """
    message = get_object_or_404(Message, id=message_id)
    replies = message.get_all_replies()  # Recursive fetching of replies
    return render(request, 'messaging/message_replies.html', {'message': message, 'replies': replies})

def unread_messages(request):
    """
    Display unread messages for the authenticated user.
    """
    unread_messages = Message.unread.unread_for_user(request.user).only('sender', 'content', 'timestamp')
    return render(request, 'messaging/unread_messages.html', {'unread_messages': unread_messages})
