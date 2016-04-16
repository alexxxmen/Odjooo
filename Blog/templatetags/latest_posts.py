# -*- coding: utf-8 -*-

from django import template
from Blog.models import Article

register = template.Library()


@register.inclusion_tag('blog/templatetag/_latest_posts.html')
def latest_posts():
    posts = Article.objects.order_by('-pub_date').filter(status='P')[:2]

    return dict(posts=posts)
