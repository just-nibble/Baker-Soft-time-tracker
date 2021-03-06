"""BakerTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# rest framework imports
from rest_framework.documentation import include_docs_urls

# project imports
from BakerTracker import settings

API_TITLE = 'Baker Tracker Docs'
API_DESCRIPTION = 'A Web API for work time tracking application.'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('docs/', include_docs_urls(
        title=API_TITLE,
        description=API_DESCRIPTION)
    ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
