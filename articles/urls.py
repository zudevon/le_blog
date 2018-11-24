from django.contrib import admin
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.article_list),
]