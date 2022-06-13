from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from blogapp.views import ArticleView

urlpatterns = [
    path("article/", ArticleView.as_view(), name="article_view"),
]