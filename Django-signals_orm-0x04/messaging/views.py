from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Message

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
    messages = Message.objects.filter(
        sender=request.user
    ).select_related('receiver', 'sender').prefetch_related('replies')

    return render(request, 'messaging/message_list.html', {'messages': messages})

def message_replies(request, message_id):
    """
    Fetch and display replies to a specific message in a threaded format.
    """
    message = get_object_or_404(Message, id=message_id)
    replies = message.get_all_replies()  # Recursive fetching of replies
    return render(request, 'messaging/message_replies.html', {'message': message, 'replies': replies})