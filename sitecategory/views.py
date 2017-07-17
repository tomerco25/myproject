from django.http import HttpResponse
from django.shortcuts import render

def tomer(request):
   return HttpResponse("<h1>tomer page</h1>")

def homepage(request):
   return HttpResponse("<h1>welcome!</h1>")

def category(request):
   return HttpResponse("<h1>this is category number 1</h1>")

def homepage_template(request):
    var1={"tomer":"tomerrrr"}
    var2="rrrr"
    return render(request,'index.html' ,var1)