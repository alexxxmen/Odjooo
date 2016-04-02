from django.shortcuts import render, get_object_or_404, Http404
from Blog.models import Article, Category


def home(request):
    articles = Article.objects.order_by('-pub_date', 'title')
    categories = Category.objects.all()
    context = {
        'title': "Blog",
        'articles': articles,
        'categories': categories
    }
    return render(request, "blog/index.html", context)


def details(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Page not found")

    return render(request, 'blog/details.html', {'article': article, 'img': '<img src="/static/img/test.png">'})


def get_by_category(request, category_id):

    articles = Article.objects.filter(category=category_id)
    return render(request, 'blog/index.html', {'articles': articles})
