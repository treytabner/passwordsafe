from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import BasePermission


class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_superuser
        )
