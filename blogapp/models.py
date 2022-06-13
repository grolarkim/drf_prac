from django.db import models
from userapp.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="카테고리", max_length=100)
    description = models.TextField(verbose_name="설명")


class Article(models.Model):
    category = models.ManyToManyField(to=Category)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField(verbose_name="내용")
