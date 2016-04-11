from django.conf.urls import url, include
from Blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^article/(?P<article_slug>.+)/$', views.article_details, name='article_details'),
    url(r'^category/(?P<category_id>\d+)/$', views.articles_by_cat, name='articles_by_cat'),
    url(r'^tag/(?P<tag_id>\d+)/$', views.articles_by_tag, name='articles_by_tag'),
    url(r'^archive/(?P<year>\d\d\d\d)/$', views.special_case, name='special_case'),
    url(r'^tinymce/', include('tinymce.urls')),

]
