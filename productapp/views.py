from datetime import date
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from productapp.models import Event
from productapp.serializers import EventSerializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response


class EventView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        query = Q(is_active = True) & Q(start_at__lte = date.today()) & Q(end_at__gte = date.today())
        event_objects = Event.objects.filter(query)
        return Response(EventSerializer(event_objects, many=True).data, status=status.HTTP_200_OK)


    def post(self, request):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_200_OK)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request):
        event = get_object_or_404(Event, id=request.data.get("id", ""))
        event_serializer = EventSerializer(event, data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_200_OK)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


