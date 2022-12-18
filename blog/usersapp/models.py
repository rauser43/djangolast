from django.db import models
from django.contrib.auth.models import AbstractUser


class BlogUser (AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)


