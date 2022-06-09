from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name="사용자 아이디", max_length=50, unique=True)
    password = models.CharField(verbose_name="비밀번호", max_length=50)
    realname = models.CharField(verbose_name="이름", max_length=50)
    birthday = models.DateField(verbose_name="생일")
    email = models.EmailField(verbose_name="이메일", max_length=100, unique=True)
    created_at = models.DateTimeField(verbose_name="가입시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정시각", auto_now=True)
    
    def __str__(self):
        return 

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name="사용자", primary_key=True)
    hobby = models.ManyToManyField(to="Hobby", verbose_name="취미", through="UserProfileHobby")
    introduction = models.TextField(verbose_name="자기소개", null=True)
    profile_image = models.ImageField(verbose_name="프로필 사진", null=True)
    
    def __str__(self):
        return 

class Hobby(models.Model):
    name = models.CharField(verbose_name="취미", max_length=50)
    
    def __str__(self):
        return 

class UserProfileHobby(models.Model):
    user_profile = models.ForeignKey
    hobby = models.ForeignKey
    
    def __str__(self):
        return 