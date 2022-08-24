from django.db import models

# Create your models here.
class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True) # 오토필드 - 자동으로 증가하는 필드
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    status = models.CharField(max_length=1, default="y") # 설문진행상태, y진행중 n 종료

class Answer(models.Model): # 설문 결과 저장 테이블
    answer_idx = models.AutoField(primary_key=True)
    survey_idx = models.IntegerField()  # 설문번호, 숫자기때문에 IntegerField
    num = models.IntegerField()         # 응답번호, 숫자기때문에 IntegerField
