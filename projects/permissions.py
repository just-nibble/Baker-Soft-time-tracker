from rest_framework import permissions


class CanEditProject(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user == obj.manager:
            return True

        if request.user.is_superuser:
            return True

        return False
