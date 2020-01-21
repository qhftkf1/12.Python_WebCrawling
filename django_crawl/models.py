from django.db import models
from .elastic_search_connection import TextIndex

# Create your models here.
class BlogData(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200, null=True, default='')
    tag = models.CharField(max_length=200, null=False, default='')
    link = models.URLField()

    def __str__(self):
        return self.title

        # indexing method of Question model
    # def indexing(self):
    #    obj = TextIndex(
    #         meta = {
    #             'id':self.id
    #         },
    #         title = self.title,
    #         date = self.date,
    #         tag = self.tag,
    #         link = self.link
    #    )
    #    obj.save()
    #    return obj.to_dict(include_meta=True)
