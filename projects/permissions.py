from rest_framework import permissions
from . models import ProjectMembers


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


class TasksPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        return False


class ProjectMemberPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.task.project.manager:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        return False
