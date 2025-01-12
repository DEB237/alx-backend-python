from django.contrib.auth.models import User
from django.http import JsonResponse

def delete_user(request):
    """
    Deletes the authenticated user's account.
    """
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({"error": "User is not authenticated"}, status=401)

    user.delete()  # Trigger post_delete signal
    return JsonResponse({"message": "User account deleted successfully"}, status=200)
