from django.urls.conf import path, re_path
from survey import views

urlpatterns = [
    re_path(r"^main$", views.main, name="main"),
    path("save", views.save, name="save"),
    path("result", views.result, name="result")
]

# name = "main" 이라 쓰는것은, html상의 링크이다.
# 정규 표현식으로 사용해도 가능, re_path(r"^main$", views.main, name="main") or path("main", views.main, name="main") 이런식으로 사용
# 페이지를 하나 만들때 마다 추가해주어야 에러가 안남