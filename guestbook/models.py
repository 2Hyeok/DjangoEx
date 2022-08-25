from django.db import models
from datetime import datetime

# Create your models here.

class Guestbook(models.Model):
    idx = models.AutoField(primary_key=True) # 자동증가값, 기본키
    name = models.CharField(null=False, max_length=50) # 이름
    email = models.CharField(null=True, max_length=50) # 이메일
    passwd = models.CharField(null=False, max_length=50) # 비밀번호
    content = models.TextField(null=False) # Textfild는 긴 문자열 일경우 사용
    postdate = models.DateTimeField(default = datetime.now, blank=True) # 작성시간