from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    link = models.URLField()
    creation_date = models.DateTimeField(default=timezone.now())
    upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=30)
    link = models.CharField(max_length=30, default="/mocklink")


class Comment(models.Model):
    author_name = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now())
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
