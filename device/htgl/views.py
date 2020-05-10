from datetime import datetime
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
   obj.type = obj2
   obj.brand = request.POST.get('brand')
   if request.POST.get('buytime') != '':
      x = request.POST.get('buytime').replace('/', '-')
      obj.buytime = datetime.strptime(x, "%Y-%m-%d")
   obj.sn = request.POST.get('sn')
   obj.memo = request.POST.get('memo')
   obj.status = request.POST.get('status')
   obj.save();
   return redirect("/device/")


def deviceAdd(request):
   if request.method == "POST":
      obj=models.Device.objects.create()
      obj.model=request.POST.get('model')
      obj.type=request.POST.get('sys')
      obj.brand=request.POST.get('brand')
      obj.sn=request.POST.get('sn')
      obj.memo=request.POST.get('memo')
      if request.POST.get('buytime') != '':
         x = request.POST.get('buytime').replace('/', '-')
         obj.buytime = datetime.strptime(x, "%Y-%m-%d")
      obj.save()
      return redirect("/device/")
   data = {}
   list = models.sys.objects.all()
   data['sys'] = list
   return render(request, 'device/add.html', data)


def cartridgeList(request):
   data = {}
   dlist = models.Cartridge.objects.all()
   data['list'] = dlist
   return render(request, 'cartridge/list.html', data)


def cartridgeDetail(request, id):
   data = {}
   dlist = models.Cartridge.objects.get(id=id)
   data['list'] = dlist
   return render(request, 'cartridge/detail.html', data)


def cartridgeAdd(request):
   if request.method == "POST":
      obj = models.Cartridge.objects.create()
      obj.model = request.POST.get('model')
      obj.brand = request.POST.get('brand')
      if request.POST.get('color') != '':
         obj.color = request.POST.get('color')
      else:
         obj.color = '黑'
      if request.POST.get('number') != '':
         obj.number = request.POST.get('number')
      else:
         obj.number = 0
      obj.save()
      return redirect("/cartridge/")
   return render(request, 'cartridge/add.html', {})


def cartridgeUpdate(request, id):
   obj = models.Cartridge.objects.get(id=id)
   obj.model = request.POST.get('model')
   obj.brand = request.POST.get('brand')
   obj.color = request.POST.get('color')
   obj.number = request.POST.get('number')
   obj.save();
   return redirect("/cartridge/")

def cartridgeDelete(request, id):
   models.Cartridge.objects.get(id=id).delete()
   return redirect("/cartrdge/")

def index(request):
   username = None
   if request.user.is_authenticated:
      username = request.user.username
   return render(request, 'index.html', {'username': username})


def htgl(request):
   return render(request, '/admin/htgl')
