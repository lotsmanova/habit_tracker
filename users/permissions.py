from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Права доступа для владельца"""

    def has_object_permission(self, request, view, obj):
        return obj == request.user
