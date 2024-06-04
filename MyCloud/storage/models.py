from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)

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
