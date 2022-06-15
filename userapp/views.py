from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from userapp.models import User, UserProfile, Hobby
from userapp.serializers import UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


class UserView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            data = UserSerializer(User.objects.all(), many=True).data
            return Response(data, status=status.HTTP_200_OK)
        return Response({"error":"로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
