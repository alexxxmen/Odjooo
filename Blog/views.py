# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from Blog.models import Article, Category, Tag


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'Start App',
        'active_menu': 'home'
    }
    return render(request, 'blog/index.html', context)


def article_details(request, article_slug):
        article = get_object_or_404(Article, slug=article_slug)
        context = {
            'article': article,
            'title': 'Start App'
        }
        return render(request, 'blog/article_details.html', context)


def articles_by_cat(request, category_id):
        articles = Article.objects.filter(category=category_id)
        context = {
            'articles': articles,
            'title': 'Start App'
        }
        return render(request, 'blog/index.html', context)


def articles_by_tag(request, tag_id):
        articles = Article.objects.filter(tags__id=tag_id)
        context = {
            'articles': articles,
            'title': 'Start App'
        }
        return render(request, 'blog/index.html', context)


def special_case(request, year):
    articles = Article.objects.filter(pub_date__year=year)
    context = {
        'articles': articles
    }
    return render(request, 'blog/index.html', context)
