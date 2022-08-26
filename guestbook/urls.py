from django.urls.conf import path
from guestbook import views

"""
urlpatterns = [
    path("list", views.list, name="list"),
    path("write", views.write, name="write"),
    path("writepro", views.writepro, name="writepro"),
    path("passwdck", views.passwdck, name="passwdck"),
    path("delete", views.delete, name="delete"),
    path("update", views.update, name="update"),
    path("read", views.read, name="read")
    ]
    
"""

# 수정후 
urlpatterns = [
        path("list", views.ListView.as_view(), name="list"),
        path("write", views.WriteView.as_view(), name="write"),
        path("passwdck", views.PasswdView.as_view(), name="passwdck"),
        path("update", views.UpdateView.as_view(), name="update")
    ]

# 이 부분은 write.html 에서 writepro를 write로 바꿨을경우 없애야한다.
# path("writepro", views.writepro, name="writepro"),