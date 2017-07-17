from django.http import HttpResponse

def tomer(request):
   return HttpResponse("<h1>tomer page</h1>")

def homepage(request):
   return HttpResponse("<h1>welcome!</h1>")

def category(request):
   return HttpResponse("<h1>this is category number 1</h1>")