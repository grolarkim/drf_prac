from django.db import models
from userapp.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="카테고리", max_length=100, unique=True)
    description = models.TextField(verbose_name="설명")
    
    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ManyToManyField(to=Category)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(verbose_name="생성시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정시각", auto_now=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(verbose_name="생성시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정시각", auto_now=True)
    
    def __str__(self):
        return f"{self.author} : {self.content}"
