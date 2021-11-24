import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=200, default="Author")
    title = models.CharField(max_length=200, default="Title")
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    age = models.PositiveIntegerField(null=True, blank=True)