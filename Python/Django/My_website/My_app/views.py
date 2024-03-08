from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(reguest):
    return HttpResponse(Page.html)