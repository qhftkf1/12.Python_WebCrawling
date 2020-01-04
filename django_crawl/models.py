from django.db import models

# Create your models here.
class BlogData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

class GoogleData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
