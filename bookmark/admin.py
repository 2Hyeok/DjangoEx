from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark # 북마크의 모델스안에 있는 북마크라는 클래스를 임포트 

class BookmarkAdmin(admin.ModelAdmin): # 모델 어드민을 상속
    # 보여줄 리스트를만듬
    list_display=("title", "url") # 튜플로 잡아줌

# 클래스는 끝
# 이제 밖에다 주어야한다
admin.site.register( Bookmark, BookmarkAdmin) # 등록해라, 북마크와 북마크 어드민을
