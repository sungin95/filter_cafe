from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )