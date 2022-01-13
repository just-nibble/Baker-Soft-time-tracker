from rest_framework import serializers

from . import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ("__all__")


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ("__all__")


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectMembers
        fields = ("__all__")
