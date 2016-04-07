# -*- coding: utf-8 -*-
from django.shortcuts import render, Http404
from Blog.models import Article, Category, Tag


def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
        'title': 'Start App'
    }
    return render(request, 'blog/index.html', context)


def article_details(request, article_id):
    pass


def articles_by_cat(request, category_id):
    pass


def articles_by_tag(request, tag_id):
    pass
