from django.conf.urls import url
from Blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^article/(?P<article_id>\d+)/$', views.article_details, name='article_detail'),
    url(r'^category/(?P<category_id>\d+)/$', views.articles_by_cat, name='articles_by_cat'),

]
