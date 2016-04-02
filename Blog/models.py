from __future__ import unicode_literals
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Category name')
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    slug = models.SlugField()
    category = models.ForeignKey(Category, default=None)

    def __str__(self):
        return self.title
