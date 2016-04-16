# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone


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
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles', related_query_name='article')
    status = models.CharField(max_length=1, choices=ARTICLE_STATUS, default='D')

    # для админки
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return self.title


class Statistic(models.Model):
    article_id = models.ForeignKey(Article, related_name='statistic')
    count = models.IntegerField(default=0)
