# C:\Users\maxiw\PycharmProjects\MyCloud_backend\MyCloud\storage\models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Уникальное имя для обратного доступа
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',  # Уникальное имя для обратного доступа
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username


class File(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    original_name = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    last_download_date = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    file_path = models.FileField(upload_to='files/')
    download_link = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.original_name
