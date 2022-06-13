from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from userapp.views import LoginView, UserView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("", UserView.as_view(), name="user"),
]