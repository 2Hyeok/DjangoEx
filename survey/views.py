from django.shortcuts import render
from django.template import loader
from survey.models import Survey, Answer
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main(request):
    template = loader.get_template("main.html")
    # 골라내야하기에 filter, 간단한 sql은 이런식으로 가능한데 복잡한 경우는 직접 sql을 작성해야함
    survey = Survey.objects.filter(status="y").order_by("-survey_idx")[0] # 설문을 다 가지고 와라, 내림차순으로
    # 딕셔너리로 가져옴
    context = {
        "survey" : survey,
        }
    return HttpResponse(template.render(context, request)) # 보내준다

@csrf_exempt # 임포트 필요
def save(request):
    template = loader.get_template("save.html")
    # 바구니를 만들필요없음, 자동으로 만들어줌
    dto = Answer(survey_idx=request.POST["survey_idx"], num=request.POST["num"]) # 엔서클레스 바구니를 바로 만들어 사용하면됨, post로 넘겼기에 post로 받음
    dto.save() # insert호출
    # 다시 main으로 돌려도 되지만
    context = {} # 비워두고 아무것도 안넘겨도 됨, dto를 넘겨도 됨, 안내멘트만 뜨고 끝나는 페이지음
    return HttpResponse(template.render(context,request))

def result( request ) :
    template = loader.get_template( "result.html" )
    survey_idx = request.GET["survey_idx"]
    ans = Survey.objects.get( survey_idx=survey_idx )
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4]
    surveylist = Survey.objects.raw("""
        select survey_idx, num, count( num ) sum_num, 
        round( ( select count(*) from survey_answer where survey_idx=an.survey_idx and num=an.num ) * 100 
        / ( select count(*) from survey_answer where survey_idx=an.survey_idx) , 1 ) rate
        from survey_answer an
        where survey_idx=%s
        group by survey_idx, num""", survey_idx )
    
    surveylist = zip( surveylist, answer )
    context = {
        "survey_idx" : survey_idx,
        "surveylist" : surveylist,
        }
    return HttpResponse( template.render( context, request ) )