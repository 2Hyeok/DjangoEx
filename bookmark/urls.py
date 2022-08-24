from django.urls.conf import path
from bookmark import views

# 홈은 이제 만들어 주어야함, 주소는 localhost:8000/bookmark/home, 이뜻은 Views 안의 home이라는 함수를 실행 하라는뜻
urlpatterns = [
    path("home", views.home, name="home"), 
]