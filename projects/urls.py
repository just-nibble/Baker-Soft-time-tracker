from django.urls import path

from . import views

app_name = "Projects"

urlpatterns = [
    path("", views.ProjectAPIView.as_view(), name="project"),
    path("<int:pk>/", views.ProjectDetailAPIView.as_view(), name="project_detail"),
    path("task/", views.TaskAPIView.as_view(), name="task"),
    path("task/<int:pk>/", views.TaskDetailAPIView.as_view(), name="task_detail"),
    path("assign/", views.ProjectMemberAPIView.as_view(), name="assign"),
    path("assign/<int:pk>/", views.ProjectMemberDetailAPIView.as_view(),
         name="assign_detail"),
]
