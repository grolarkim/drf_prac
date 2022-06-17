from django.contrib import admin
from productapp.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active")

admin.site.register(Event)
