from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from productapp.views import EventView

urlpatterns = [
    path("event/", EventView.as_view(), name="event_view"),
]