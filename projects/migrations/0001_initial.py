# Generated by Django 3.2 on 2022-01-13 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('projected_completion_time', models.DateTimeField(null=True)),
                ('actual_completion_time', models.DateTimeField(null=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(max_length=255, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='task/attachment')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('assigned', 'assigned'), ('completed', 'completed')], max_length=15, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.task')),
            ],
        ),
    ]
