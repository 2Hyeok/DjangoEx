from django.urls.conf import path
from guestbook import views

urlpatterns = [
    path("list", views.list, name="list"),
    path("write", views.write, name="write"),
    path("writepro", views.writepro, name="writepro"),
    path("passwdck", views.passwdck, name="passwdck"),
    path("delete", views.delete, name="delete"),
    path("update", views.update, name="update")
    ]