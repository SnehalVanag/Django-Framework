from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hey this is home page")

def about(request):
    return HttpResponse("Hey this is about page")
