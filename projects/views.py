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
