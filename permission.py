from rest_framework.permissions import BasePermission

class PeracikPermission(BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, 'peracik'):
            return True
        return False
