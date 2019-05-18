from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request,"home.html",{"sat":"satish"})

def add(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1+val2
    return render(request,"add.html",{"result":res})


def front(request):
    return render(request,"front.html")




def index(request):
    return render(request,"index.html")



