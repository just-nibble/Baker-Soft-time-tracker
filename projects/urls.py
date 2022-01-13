from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProjectAPIView.as_view()),
    path("<int:pk>/", views.ProjectDetailAPIView.as_view()),
    path("task/", views.TaskAPIView.as_view()),
    path("task/<int:pk>/", views.TaskDetailAPIView.as_view()),
    path("assign/", views.ProjectMemberAPIView.as_view()),
    path("assign/<int:pk>/", views.ProjectMemberDetailAPIView.as_view()),
]
