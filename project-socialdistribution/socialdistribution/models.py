from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)