from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name="사용자 아이디", max_length=50, unique=True)
    password = models.CharField(verbose_name="비밀번호", max_length=128)
    realname = models.CharField(verbose_name="이름", max_length=50, null=True)
    birthday = models.DateField(verbose_name="생일", null=True)
    age = models.IntegerField(verbose_name="나이", default=0, null=True)
    email = models.EmailField(verbose_name="이메일", max_length=100, null=True)
    created_at = models.DateTimeField(verbose_name="가입시각", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정시각", auto_now=True)
    
    is_active = models.BooleanField(default=True) 
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label): 
        return True
    
    @property
    def is_staff(self): 
        return self.is_admin


class Hobby(models.Model):
    name = models.CharField(verbose_name="취미", max_length=50)
    
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name="사용자", primary_key=True)
    hobby = models.ManyToManyField(to="Hobby", verbose_name="취미", through="UserProfileHobby")
    introduction = models.TextField(verbose_name="자기소개", null=True)
    profile_image = models.ImageField(verbose_name="프로필 사진", null=True)
    
    def __str__(self):
        return self.user.username

class UserProfileHobby(models.Model):
    user_profile = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    hobby = models.ForeignKey(to=Hobby, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_profile.user.username