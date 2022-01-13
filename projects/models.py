from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=255, null=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    projected_completion_time = models.DateTimeField(null=True)
    actual_completion_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    attachment = models.FileField(
        upload_to="task/attachment", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=15, null=True, default="pending")

    def __str__(self):
        return self.title


class ProjectMembers(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.task) + ": " + str(self.member)


@receiver(post_save, sender=ProjectMembers)
def change_to_assigned(sender, instance, **kwargs):
    instance.task.status = "assigned"
    instance.task.save()
