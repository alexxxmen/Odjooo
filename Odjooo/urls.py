from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('Blog.urls', namespace='Blog')),
    url(r'^admin/', admin.site.urls),
]
