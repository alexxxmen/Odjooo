# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Тег")
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Category name')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')

    def __unicode__(self):
        return self.name


class Article(models.Model):
    ARTICLE_STATUS = (
        ('D', 'Черновик'),
        ('P', 'Опубликовано'),
        ('E', 'Устарел'),
    )
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    text = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='categories')
    tags = models.ManyToManyField(Tag, related_name='tags', related_query_name='tag')
    status = models.CharField(max_length=1, choices=ARTICLE_STATUS, default='D')

    def __unicode__(self):
        return self.title
