from dataclasses import field
from rest_framework import serializers
from productapp.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "thumbnail", "description", "start_at", "end_at", "is_active"]