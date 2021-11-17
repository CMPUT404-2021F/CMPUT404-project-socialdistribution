from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class Post(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=200, default="Author")
    title = models.CharField(max_length=200, default="Title")
    text = models.TextField()

class CustomUser(AbstractUser):
    # https://stackoverflow.com/questions/16925129/generate-unique-id-in-django-from-a-model-field/30637668
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)