# -*- coding: utf-8 -*-
import time
from django.shortcuts import render, get_object_or_404
from Blog.models import Article, Category, Tag, Statistic
from calendar import month_name
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def home(request):
    articles = Article.objects.order_by('-pub_date')
    paginator = Paginator(articles, 3)

    try:
        page = int(request.GET.get('page', 1))
    except ValueError: page = 1
    try:
        articles = paginator.page(page)
    except (InvalidPage, EmptyPage):
        articles = paginator.page(paginator.num_pages)

    context = {
        'articles': articles,
        'title': 'Start App',
        'active_menu': 'home',
        'months': monthly_archive_list(),
        # 'paginator': paginator
    }
    return render(request, 'blog/index.html', context)


def article_details(request, article_slug):
        article = get_object_or_404(Article, slug=article_slug)

        try:    # Count for view article
            stat_obj = Statistic.objects.get(article_id=article.id)
            stat_obj.count += 1
            stat_obj.save()
        except Statistic.DoesNotExist:
            stat_obj = Statistic.objects.create(article_id=article.id, count=1)
            stat_obj.save()

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


def monthly_archive_list():
    if not Article.objects.all(): return []
    year, month = time.localtime()[:2]
    first = Article.objects.order_by('pub_date')[0]
    fyear = first.pub_date.year
    fmonth = first.pub_date.month
    months = []

    for y in range(year, fyear-1, -1):
        start = 12
        end = 0
        if y == year: start = month
        if y == fyear: end = fmonth-1

        for m in range(start, end, -1):
            months.append((y, m, month_name[m]))
    return months


def monthly_archive(request, year, month):
    posts = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {
        'articles': posts,
        'months': monthly_archive_list()
    }
    return render(request, 'blog/index.html', context)
