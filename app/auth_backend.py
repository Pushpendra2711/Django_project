from django.contrib.auth.backends import BaseBackend
from .models import loc_user

class LocUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Use your custom model's authenticate method
            user = loc_user.objects.get(username=username)
            if user and user.check_password(password):
                return user
        except loc_user.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return loc_user.objects.get(pk=user_id)
        except loc_user.DoesNotExist:
            return None
