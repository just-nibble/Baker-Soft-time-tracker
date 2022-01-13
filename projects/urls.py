from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectAPIView.as_view()),
    path("<int:pk>/", views.ProjectDetailAPIView.as_view()),
]
