from django.contrib import admin
from . import views
from django.conf.urls import url


app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail')  # Regrex format... easier in Django2
]