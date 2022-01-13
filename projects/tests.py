from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from . import models
from accounts.models import CustomUser
# Create your tests here.


class ProjectModelTestcase(TestCase):
    @classmethod
    def test_setUpTestData(cls):
        user = CustomUser.objects.create(username="TestUserName")
        models.Project.objects.create(
            title="Peter Project", manager=user)


class TaskModelTestcase(TestCase):
    @classmethod
    def test_setUpTestData(cls):
        user = CustomUser.objects.create(username="TestUserName")
        project = models.Project.objects.create(
            title="Peter Project", manager=user)
        models.Task.objects.create(
            title="TestTitleTest", description="TestDescription", project=project)


class ProjectMemberModelTestcase(TestCase):
    @classmethod
    def test_setUpTestData(cls):
        user = CustomUser.objects.create(username="TestUserName")
        project = models.Project.objects.create(
            title="Peter Project", manager=user)
        task = models.Task.objects.create(
            title="TestTitleTest", description="TestDescription", project=project)
        models.ProjectMembers(task=task, member=user)
