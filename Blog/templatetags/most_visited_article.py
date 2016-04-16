# -*- coding: utf-8 -*-

from django import template
from Blog.models import Article

register = template.Library()


@register.inclusion_tag('blog/templatetag/_most_visited_article.html')
def most_visited():
    articles = Article.objects.order_by('-statistic__count')[:5]
    return locals()
