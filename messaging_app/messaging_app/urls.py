from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),  # Include the routes from chats app
    path('api-auth/', include('rest_framework.urls')),  # Add this line for api-auth
]
