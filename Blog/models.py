from __future__ import unicode_literals
from django.db import models


class Manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField()
    tags = models.ForeignKey(Manager)

    def __str__(self):
        return self.title