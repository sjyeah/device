from django.shortcuts import render

# Create your views here.


def device(request):
    return render(request, 'device.html')


def index(request):
    username = None
    if request.user.is_authenticated:
            username = request.user.username
    return render(request, 'index.html', {'username': username})
