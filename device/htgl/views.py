from django.shortcuts import render, redirect
from . import models


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
   list2 = models.sys.objects.all()
   data['sys'] = list2
   return render(request, 'device/detail.html', data)


def deviceDelete(request, id):
   models.Device.objects.get(id=id).delete()
   return redirect("/device/")


def deviceUpdate(request, id):
   obj = models.Device.objects.get(id=id)
   obj2 = models.sys.objects.get(id=request.POST.get('type'))
   obj.model = request.POST.get('model')
   obj.type=obj2
   obj.brand= request.POST.get('brand')
   if request.POST.get('buytime') !='':
      obj.buytime= request.POST.get('buytime')
   obj.sn = request.POST.get('sn')
   obj.memo = request.POST.get('memo')
   obj.status = request.POST.get('status')
   obj.save();
   return redirect("/device/")


def deviceAdd(request):
   if request.method == "POST":
      obj= models.sys.objects.get(id=1)
      models.Device.objects.create(model = request.POST.get('model'),type=obj,brand= request.POST.get('brand'))
      return redirect("/device/")
   data = {}
   list=models.sys.objects.all()
   data['sys']=list
   return render(request, 'device/add.html', data)


def index(request):
   username = None
   if request.user.is_authenticated:
      username = request.user.username
   return render(request, 'index.html', {'username': username})


def htgl(request):
   return render(request, '/admin/htgl')
