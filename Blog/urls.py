from django.conf.urls import url
from Blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^article/(?P<article_id>\d+)/$', views.details, name='details'),
    url(r'^category/(?P<category_id>\d+)/$', views.get_by_category, name='get_by_category'),

]
