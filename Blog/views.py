# -*- coding: utf-8 -*-
from django.shortcuts import render, Http404
from Blog.models import Article, Category, Tag


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'Start App',
        'active_menu': 'home'
    }
    return render(request, 'blog/index.html', context)


def article_details(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        context = {
            'article': article,
            'title': 'Start App'
        }
        return render(request, 'blog/article_deteils.html', context)
    except Article.DoesNotExist:
        raise Http404


def articles_by_cat(request, category_id):
    try:
        articles = Article.objects.filter(category=category_id)
        context = {
            'articles': articles,
            'title': 'Start App'
        }
        return render(request, 'blog/index.html', context)
    except Article.DoesNotExist:
        raise Http404


def articles_by_tag(request, tag_id):
    try:
        articles = Article.objects.filter(tags__id=tag_id)
        context = {
            'articles': articles,
            'title': 'Start App'
        }
        return render(request, 'blog/index.html', context)
    except Article.DoesNotExist:
        raise Http404
