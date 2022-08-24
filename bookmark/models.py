from django.db import models

# Create your models here.

class Bookmark(models.Model): # 모델을 상속 받으면됨
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True) # 유니크 를 줌
    def __str__(self):
        return self.title