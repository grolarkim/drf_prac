from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status


# class CustomAdultPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         result = bool(user and user.is_authenticated and user.age >= 18)
        # return result


class UserApiView(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


# class UserAdultAPIView(APIView):
#     permission_classes = [CustomAdultPermission]
#     def get(self, request):
#         return Response({"msg":"get success"})