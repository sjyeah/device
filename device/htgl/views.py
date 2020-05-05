from django.shortcuts import render

# Create your views here.


def device(request):
    return render(request, 'device.html')


def index(request):
    userinfo = models.userinfo
    return render(request,'index.html',{"userinfo":userinfo})
