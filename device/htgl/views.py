from django.shortcuts import render, redirect
from . import models
from django.template import RequestContext


# Create your views here.


def deviceList(request):
   data = {}
   dlist = models.Device.objects.all()
   data['list'] = dlist
   return render(request, 'device/list.html', data)


def deviceDetail(request, id):
   data = {}
   dlist = models.Device.objects.get(id=id)
   data['list'] = dlist
   return render(request, 'device/detail.html', data)


def deviceDelete(request, id):
   models.Device.objects.get(id=id).delete()
   return redirect("/device/list.html")


def deviceUpdate(request, id):
   obj = models.Device.objects.get(id=id)
   obj.model = request.POST.get('model')
   obj.save();
   return redirect("/device/list.html")


def index(request):
   username = None
   if request.user.is_authenticated:
      username = request.user.username
   return render(request, 'index.html', {'username': username})


def htgl(request):
   return render(request, '/admin/htgl')
