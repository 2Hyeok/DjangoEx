from django.shortcuts import render, redirect
from django.template import loader
from guestbook.models import Guestbook
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# 글목록
def list( request ) :
    template = loader.get_template( "list.html" )
    gbcount = Guestbook.objects.count() # 게스트북이라는 클래스를 사용함
    gblist = Guestbook.objects.order_by( "-idx" ) # 전체를 가져오는데 내림차순으로 가져와라, 최신순으로 맨위에 표시하기위헤
    context = {
        "gbcount" : gbcount,
        "gblist" : gblist
        }
    return HttpResponse( template.render( context, request ) )

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


# 삭제
def delete(request):
    idx = request.GET["idx"]
    Guestbook.objects.get(idx=idx).delete()
    return redirect("list")

def update(request):
    pass