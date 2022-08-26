from django.shortcuts import render, redirect
from django.template import loader
from guestbook.models import Guestbook
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
# 글목록
"""
def list( request ) :
    template = loader.get_template( "list.html" )
    gbcount = Guestbook.objects.count() # 게스트북이라는 클래스를 사용함
    gblist = Guestbook.objects.order_by( "-idx" ) # 전체를 가져오는데 내림차순으로 가져와라, 최신순으로 맨위에 표시하기위헤
    context = {
        "gbcount" : gbcount,
        "gblist" : gblist
        }
    return HttpResponse( template.render( context, request ) )
"""
from django.views.generic import View

# 페이지 넘기는 기능 -> 리스트 출력
class ListView(View):
    def get(self, request): # 디비 처리할것이 없기에 GET방식으로 처리를함
        template = loader.get_template( "list.html" )
        gbcount = Guestbook.objects.count() # 게스트북이라는 클래스를 사용함
        gblist = Guestbook.objects.order_by( "-idx" ) # 전체를 가져오는데 내림차순으로 가져와라, 최신순으로 맨위에 표시하기위헤
        context = {
            "gbcount" : gbcount,
            "gblist" : gblist
        }
        return HttpResponse( template.render( context, request ) )
    def post(self, request): # post 방식은없기에 pass
        pass
"""
# 글작성 페이지
def write(request):
    template = loader.get_template("write.html")
    context={}
    return HttpResponse(template.render(context, request)) # 넘길 데이터가 없기에 그냥 context만 써주면됨

# 글 작성 실행
@csrf_exempt
def writepro(request):
    # 바구니 생성
    dto = Guestbook(
        name = request.POST["name"],
        email = request.POST["email"],
        passwd = request.POST["passwd"],
        content = request.POST["content"]
        ) # 생성자
    dto.save() #insert 호출
    # 데이터를 넘길때 리스트로 넘겨야하는데 데이터를 넘겨야한다면 HTTP를 해주어야하지만
    return redirect("list") # 저장만해서 list로 바로 출력할 것이기 때문에 넘길 경우에만 redirect 사영해서 넘김
"""
# 글 작성
class WriteView(View):
    # csrf 토큰 처리 
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WriteView,self).dispatch(request, *args, **kwargs)
    
    def get(self,request): # 페이지만 넘기는 방식이기에 get방식
        template = loader.get_template("write.html")
        context={}
        return HttpResponse(template.render(context, request)) # 넘길 데이터가 없기에 그냥 context만 써주면됨
    
    def post(self,request): # 처리를 해주는것 이기 때문에 post 방식으로
    # 바구니 생성
        dto = Guestbook(
            name = request.POST["name"],
            email = request.POST["email"],
            passwd = request.POST["passwd"],
            content = request.POST["content"]
            ) # 생성자
        dto.save() #insert 호출
        # 데이터를 넘길때 리스트로 넘겨야하는데 데이터를 넘겨야한다면 HTTP를 해주어야하지만
        
        # 하지만 redirect는 get방식으로 넘어감
        return redirect("list") # 저장만해서 list로 바로 출력할 것이기 때문에 넘길 경우에만 redirect 사용해서 넘김
"""
# 비밀번호 확인 -> 수정 및 삭제 페이지
@csrf_exempt
def passwdck(request):
    template = loader.get_template("edit.html") # 수정페이지
    idx = request.POST["idx"]
    passwd = request.POST["passwd"]
    dto = Guestbook.objects.get(idx=idx) # 바구니에서 확인
    context = { # 수정할 것이기에 바구니를 통채로 넘김
        "dto" : dto
        }
    if passwd == dto.passwd : # 바구니와 입력한 것이 같은지 확인 
        # 같으면 처리페이지로 넘어가도록
        return HttpResponse(template.render(context, request))
    else :
        return redirect("list")
"""
class PasswdView(View):
    # csrf 토큰 처리 
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PasswdView,self).dispatch(request, *args, **kwargs)
    
    # get방식은 필요 없어서 post만 구현해도 상관없음
    def post(self,request):
        template = loader.get_template("edit.html") # 수정페이지
        idx = request.POST["idx"]
        passwd = request.POST["passwd"]
        dto = Guestbook.objects.get(idx=idx) # 바구니에서 확인
        context = { # 수정할 것이기에 바구니를 통채로 넘김
            "dto" : dto
            }
        if passwd == dto.passwd : # 바구니와 입력한 것이 같은지 확인 
            # 같으면 처리페이지로 넘어가도록
            return HttpResponse(template.render(context, request))
        else :
            return redirect("/guestbook/list")
        

"""
# 삭제
def delete(request):
    idx = request.GET["idx"] # get방식이기에 get으로 써줌
    Guestbook.objects.get(idx=idx).delete()
    return redirect("list") # 리스트로 돌아감


# 수정
@csrf_exempt
def update(request):
    idx = request.POST["idx"]
    dto = Guestbook.objects.get(idx=idx)
    newdto = Guestbook(
        idx = dto.idx,
        name = dto.name, # 이름은 수정 못하기에 넘어온 이름을 그대로 넣음
        email = request.POST["email"],
        passwd = request.POST["passwd"],
        content = request.POST["content"]
        )
    # idx가 primary key이기때문에 중복값이 들어가지 않음
    # 하지만 save를 한번더 호출하면 update가됨 -> 덮어쓴다의 개념
    # save는 insert하는 기능도 있지만 한번더 호출하면 update하는 기능도 가지고있음
    newdto.save()
    return redirect("list") # 리스트로 돌아감
    
"""
# 삭제는 get방식
# 수정은 post방식으로
# 하나로 묶을것임, 하지만 따로하는것이 옳은방법
# 프로젝트 적용시에는 수정 삭제 클래스를 따로 만들것
class UpdateView(View):
    # csrf 토큰 처리 
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateView,self).dispatch(request, *args, **kwargs)
    
    def get(self,request): # delete
        idx = request.GET["idx"] # get방식이기에 get으로 써줌
        Guestbook.objects.get(idx=idx).delete()
        return redirect("list") # 리스트로 돌아감 
    
    def post(self,request): # update
        idx = request.POST["idx"]
        dto = Guestbook.objects.get(idx=idx)
        newdto = Guestbook(
            idx = dto.idx,
            name = dto.name, # 이름은 수정 못하기에 넘어온 이름을 그대로 넣음
            email = request.POST["email"],
            passwd = request.POST["passwd"],
            content = request.POST["content"]
            )
        # idx가 primary key이기때문에 중복값이 들어가지 않음
        # 하지만 save를 한번더 호출하면 update가됨 -> 덮어쓴다의 개념
        # save는 insert하는 기능도 있지만 한번더 호출하면 update하는 기능도 가지고있음
        newdto.save()
        return redirect("list") # 리스트로 돌아감

#------------------------------------------------------------------------------------------------
from django import forms

# 임의로 폼을 만들어줌
# 대신 건드릴 수 없음
# 많이 쓰는 방식은 아님
# 만들어진 폼을 넘기는 방식
class Readfrom(forms.Form):
    name = forms.CharField(label="name", max_length="50" )
    email = forms.EmailField(label="email", max_length="50")
    passwd = forms.CharField(label="passwd", max_length="12", widget=forms.PasswordInput, required=True)
    content = forms.CharField(label="content", widget=forms.Textarea)
    # label 에는 한글을 넣을 수 없음
    
# 이동을 위한 함수 생성
def read(request) :
    template = loader.get_template("read.html")
    content = {
        "form" : Readfrom
        }
    return HttpResponse(template.render(content, request))