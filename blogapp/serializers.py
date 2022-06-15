from rest_framework import serializers
from blogapp.models import Article, Category, Comment
from userapp.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    author = UserSerializer()
    
    class Meta:
        model = Article
        fields = ["author", "category", "title", "content"]


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    author = UserSerializer()
    
    class Meta:
        model = Comment
        fields = ["article", "author", "content"]