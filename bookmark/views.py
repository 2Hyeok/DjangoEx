from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse # from django.http import HttpResponse 해도 상관없음
from bookmark.models import Bookmark

# Create your views here.
def home(request): # 요청의 대한 데이터를 가지고있음
    # 출력 페이지를 가져올것
    # template
    template = loader.get_template("home.html") # 템플릿 파일의 이름지정
    urllist = Bookmark.objects.order_by("title") # 데이터를 가져와 title로 정렬해라, 리스트로 만들것
    urlcount = Bookmark.objects.all().count() # 전체를 다 가져옴, count 를 사용해서 갯수를 가져올것임
    
    # 이제 뷰 페이지로 데이터를 넘겨야함
    # 튜플로 만들어줌
    context = {
        "urllist" : urllist,
        "urlcount" : urlcount,
        }
    return HttpResponse(template.render(context,request)) # response를 이용해 데이터를 넘김, render 사용