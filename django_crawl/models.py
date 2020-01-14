from django.db import models

# Create your models here.
class BlogData(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200, null=True, default='')
    tag = models.CharField(max_length=200, null=False, default='')
    link = models.URLField()
