from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from blogapp.models import Category, Article
from datetime import timedelta
from django.utils import timezone

class RegistedMoreThanThreeDayUser(permissions.BasePermission):
    # 가입 3분지나야 가능
    message = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다.'
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.created_at < (timezone.now() - timedelta(minutes=3)))

class ArticleView(APIView):
    permission_classes = [RegistedMoreThanThreeDayUser]
    
    def post(self, request):
        if request.user.is_authenticated:
            title = request.data.get("title", "")
            content = request.data.get("content", "")
            categories = request.data.get("category_id", "")
            author_id = request.user.id
            
            category = categories.split(",")
            category_list = []
            for cate in category:
                cat, status = Category.objects.get_or_create(cate)
                category_list.append(cat)
            new_article = Article(title=title, content=content, author_id=author_id)
            new_article.save()
            new_article.category.add(*category_list)
            
            
            return Response({"msg":"게시글이 작성되었습니다."}, status=status.HTTP_201_CREATED)
        return Response({"error":"로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)