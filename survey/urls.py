from django.urls.conf import path
from survey import views

urlpatterns = [
    path("main", views.main, name="main"),
    path("save", views.save, name="save"),
    path("result", views.result, name="result")
]

# 정규 표현식으로 사용해도 가능
# 페이지를 하나 만들때 마다 추가해주어야 에러가 안남