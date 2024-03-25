from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(reguest):
    return HttpResponse("Hellow word")


# def minha_view(request):
#     return render(request, 'My_website/Page.html')