from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import serializers, models, permissions
# Create your views here.


class ProjectAPIView(ListCreateAPIView):
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.CanEditProject]
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()


class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.CanEditProject]
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()


class TaskAPIVIew(ListCreateAPIView):
    permission_classes = [permissions.TasksPermissions]
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.TasksPermissions]
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class ProjectMemberAPIView(ListCreateAPIView):
    permission_classes = [permissions.TasksPermissions]
    serializer_class = serializers.ProjectMemberSerializer
    queryset = models.ProjectMembers.objects.all()


class ProjectMemberDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.TasksPermissions]
    serializer_class = serializers.ProjectMemberSerializer
    queryset = models.ProjectMembers.objects.all()
