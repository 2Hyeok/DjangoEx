from django.contrib import admin
from survey.models import Survey

# Register your models here.

# 관리자가 직접 질문을 넣어야함
class SurveyAdmin(admin.ModelAdmin):
    # 원래는 웹 페이지 따로 만들어야함
    list_display = ("question", "ans1", "ans2", "ans3", "ans4", "status") # 컬럼 이름을 주어야함
    # 여기까지가 설정 끝
admin.site.register(Survey ,SurveyAdmin)

# answer 가 필요하면 answer를 따로 정의 해 주어야함