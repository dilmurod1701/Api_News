from django.db import models

# Create your models here.


class NewsData(models.Model):
    title = models.CharField(max_length=2000)
    content = models.TextField(null=True)
    link = models.URLField(max_length=2000)
    day = models.CharField(max_length=12)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return self.title
