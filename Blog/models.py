# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Тег")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Category name')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags', related_query_name='tag')

    def __str__(self):
        return self.title
