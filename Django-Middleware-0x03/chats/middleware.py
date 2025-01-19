import logging
from datetime import datetime
from django.http import HttpResponseForbidden
from time import time

class RequestLoggingMiddleware:
    """
    Middleware to log user requests.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        handler = logging.FileHandler("requests.log")
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        self.logger.info(log_message)
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    """
    Middleware to restrict access based on time.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        if current_hour >= 21 or current_hour < 6:  # Outside 9 PM to 6 AM
            return HttpResponseForbidden("Access to the chat is restricted during this time.")
        return self.get_response(request)
    

class OffensiveLanguageMiddleware:
    """
    Middleware to limit messages per IP address to 5 per minute.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_requests = {}

    def __call__(self, request):
        if request.method == "POST":
            ip = self.get_client_ip(request)
            current_time = time()

            if ip not in self.ip_requests:
                self.ip_requests[ip] = []

            # Clean up old requests
            self.ip_requests[ip] = [
                timestamp for timestamp in self.ip_requests[ip]
                if current_time - timestamp < 60
            ]

            # Check if limit is exceeded
            if len(self.ip_requests[ip]) >= 5:
                return HttpResponseForbidden("Message limit exceeded. Try again later.")

            # Add current request
            self.ip_requests[ip].append(current_time)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')

class RolePermissionMiddleware:
    """
    Middleware to enforce user role permissions for specific actions.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow access if the user is an admin or moderator
        if request.path.startswith("/admin/") or request.path.startswith("/moderator/"):
            if not request.user.is_authenticated or not request.user.is_staff:
                return HttpResponseForbidden("You do not have permission to access this resource.")
        return self.get_response(request)


