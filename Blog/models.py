from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title
