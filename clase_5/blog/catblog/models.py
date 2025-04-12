from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(null=False, primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    publish_date = models.DateField(default=timezone.now)
    active_post = models.BooleanField(default=True)
