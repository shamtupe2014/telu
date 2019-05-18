from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('add',views.add,name="add"),
    path("front",views.front,name="front"),
    path("index/",views.index,name="index")

]
