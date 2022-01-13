from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import serializers, models, permissions
# Create your views here.


class ProjectAPIView(ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    filterset_fields = ["title",
                        "manager__username",
                        "start_time",
                        "projected_completion_time",
                        "actual_completion_time"]

    search_fields = ["title",
                     "manager__username",
                     "start_time",
                     "projected_completion_time",
                     "actual_completion_time"]

    ordering_fields = ["title",
                       "manager__username",
                       "start_time",
                       "projected_completion_time",
                       "actual_completion_time"]

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.CanEditProject]
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()


class TaskAPIView(ListCreateAPIView):
    queryset = models.Task.objects.all()
    permission_classes = [permissions.TasksPermissions]
    serializer_class = serializers.TaskSerializer
    filterset_fields = ["title", "description", "project__title", "status", ]

    search_fields = ["title", "description", "project__title", "status", ]

    ordering_fields = ["title", "description", "project__title", "status", ]


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.TasksPermissions]
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class ProjectMemberAPIView(ListCreateAPIView):
    queryset = models.ProjectMembers.objects.all()
    permission_classes = [permissions.TasksPermissions]
    serializer_class = serializers.ProjectMemberSerializer
    filterset_fields = ["task", "member", ]

    search_fields = ["task", "member", ]

    ordering_fields = ["task", "member", ]


class ProjectMemberDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.TasksPermissions]
    serializer_class = serializers.ProjectMemberSerializer
    queryset = models.ProjectMembers.objects.all()
