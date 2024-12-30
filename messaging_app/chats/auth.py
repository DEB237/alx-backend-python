from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom Token View to add extra information if needed.
    """
    pass