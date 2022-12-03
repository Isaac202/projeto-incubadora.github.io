from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"site/index.html")

def apoie(request):
    return render(request,"site/apoie.html")