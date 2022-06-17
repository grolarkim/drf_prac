from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(verbose_name="제목",max_length=128)
    thumbnail = models.ImageField(verbose_name="썸네일")
    description = models.TextField(verbose_name="설명")
    created_at = models.DateTimeField(verbose_name="등록일자",auto_now_add=True)
    start_at = models.DateField(verbose_name="노출 시작일")
    end_at = models.DateField(verbose_name="노출 종료일")
    is_active = models.BooleanField(verbose_name="활성화 여부")
    
    def __str__(self):
        return self.title