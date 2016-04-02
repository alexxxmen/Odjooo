from django.shortcuts import render, get_object_or_404
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
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/details.html', {'article': article})
