from django.shortcuts import render
from Blog.models import Article


def home(request):
    articles = Article.objects.all()
    context = {
        'title': "Blog",
        'articles': articles,
        'str': "string",
    }
    return render(request, "blog/index.html", context)
