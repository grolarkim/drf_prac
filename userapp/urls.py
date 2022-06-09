from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from userapp.views import UserAPIView, UserAdultAPIView

urlpatterns = [
    path("", UserAPIView.as_view(), name="userapi"),
    path("adult/", UserAdultAPIView.as_view(), name="useradultapi"),
]