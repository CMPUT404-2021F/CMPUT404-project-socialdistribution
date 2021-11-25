from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200, default="Title")
    text = models.TextField()

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('post:post_detail', args=[str(self.id)])