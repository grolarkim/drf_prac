from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class CustomAdultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.age >= 18)
        return result
    

# Create your views here.
class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        return Response({"msg":"get success"})

class UserAdultAPIView(APIView):
    permission_classes = [CustomAdultPermission]
    def get(self, request):
        return Response({"msg":"get success"})