import os
import random
import string
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login, authenticate
from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse, JsonResponse, HttpRequest
import simplejson
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.


def borrowAdd(request):
   if request.method == "POST":
      data = request.POST
   else:
      data = request.GET
      sysobj = models.sys.objects.get(id=13)
      devices = models.Device.objects.filter(status=sysobj).order_by('type')
      data = {'dlist': devices}
      return render(request, 'borrow/add.html', data)


def borrowList(request):
   if request.method == "GET":
      dlist = models.RecordBorrow.objects.all()
   if request.method == "POST":
      req = request.POST
      dep = req.get('')
   data = {'list': dlist}
   return render(request, 'device/list.html', data)


def borrowAudit(request):
   obj = models.RecordBorrow.objects.get(id=request.POST.get('bid'))
   obj2 = models.sys.objects.get(id=16)
   if obj.status != obj2:
      obj.status = obj2
      obj.save();
      for dev in obj.devices.all():
         x = models.RecordDevice.objects.create()
         x.did = dev
         x.borrowid = obj
         x.status = models.sys.objects.get(id=18)
         x.save()
   return redirect("/device/")


def borrowAudit2(request, id):
   obj3 = models.sys.objects.get(id=16)
   obj = models.RecordBorrow.objects.get(id=id)
   if obj.status != obj3:
      obj2 = models.sys.objects.get(id=17)
      obj.status = obj2
      obj.save();
   return redirect("/device/")


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
      obj = models.Device.objects.create()
      obj.model = request.POST.get('model')
      obj.type = request.POST.get('sys')
      obj.brand = request.POST.get('brand')
      obj.sn = request.POST.get('sn')
      obj.memo = request.POST.get('memo')
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


def htgl(request):
   return render(request, '/admin/htgl')


def index(request):
   username = None
   if request.user.is_authenticated:
      username = request.user.first_name
   return render(request, 'index.html', {'username': username})


def login_user(request):
   if request.method == "POST":
      user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
      if user is not None:
         if user.is_active:
            login(request, user)
            return redirect('/index')
         else:
            return render(request, 'login.html', {'msg': '账号已经禁用'})
      else:
         return render(request, 'login.html', {'msg': '用户名或者密码不正确'})
   else:
      return render(request, 'login.html')


@login_required
def logout(request):
   auth_logout(request)
   return redirect('/login')


# region API
@csrf_exempt
def people_list(request: HttpRequest):
   if request.method == "POST":
      try:
         result = simplejson.loads(request.body)
         if result["PWD"] == "%^*IFGbgi2332322253gr":
            dlist = models.people.objects.all()
            data = {'people': serializers.serialize("json", dlist, ensure_ascii=False)}
            return JsonResponse(data, charset='utf-8', json_dumps_params={'ensure_ascii': False})
         else:
            return JsonResponse({'msg': 'password'})
      except Exception as e:
         return JsonResponse({'msg': str(e)})


@csrf_exempt
def people_update(request):
   try:
      if request.GET.get("PWD") == "%^*IFGbgi2332322253gr":
         p = models.people.objects.get(id=request.GET.get("id"))
         if p.zt == 0:
            p.zt = 1
         else:
            p.zt = 0
         p.save()
         dlist = models.people.objects.all()
         data = {'people': serializers.serialize("json", dlist, ensure_ascii=False)}
         return JsonResponse(data, charset='utf-8', json_dumps_params={'ensure_ascii': False})
      else:
         return HttpResponse("password")
   except Exception as e:
      return HttpResponse(str(e))


@csrf_exempt
def people_search(request: HttpRequest):
   if request.method == "POST":
      try:
         result = simplejson.loads(request.body)
         if result["PWD"] == "%^*IFGbgi2332322253gr":
            dlist = models.people.objects.filter(name__contains=result["name"])
            if result["zzt"] == "0":
               dlist = dlist.filter(zt=0)
            data = {'people': serializers.serialize("json", dlist, ensure_ascii=False)}
            return JsonResponse(data, charset='utf-8', json_dumps_params={'ensure_ascii': False})
         else:
            return JsonResponse({'msg': 'password'})
      except Exception as e:
         return JsonResponse({'msg': str(e)})


@csrf_exempt
def advice_add(request):
   try:
      if request.method == "POST":
         result = simplejson.loads(request.body)
         if result["PWD"] == "%^*IFGbgi2332322253gr":
            advice = models.advice()
            advice.name = result["name"]
            advice.content = result["content"]
            advice.userid = result["userid"]
            advice.department = result["department"]
            if result["pic"]:
               advice.pic = result["pic"]
            advice.save()
            return HttpResponse('ok')
         else:
            return HttpResponse('password')
   except Exception as e:
      return HttpResponse(str(e))


@csrf_exempt
def advice_list(request: HttpRequest):
   if request.method == "POST":
      try:
         result = simplejson.loads(request.body)
         if result["PWD"] == "%^*IFGbgi2332322253gr":
            if result["zt"] == "0":
               dlist = models.advice.objects.all()
            else:
               dlist = models.advice.objects.filter(userid=result["userid"])
            data = {'advice': serializers.serialize("json", dlist, ensure_ascii=False)}
            return JsonResponse(data, charset='utf-8', json_dumps_params={'ensure_ascii': False})
         else:
            return JsonResponse({'msg': 'password'})
      except Exception as e:
         return JsonResponse({'msg': str(e)})


@csrf_exempt
def advice_addpic(request):
   if request.method == "POST":
      myFile = request.FILES.get("file", None)
      if myFile:
         dir = '/root/zzb/device/files/upload/advice/'
         ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
         type = os.path.splitext(myFile.name)[1]
         fname = ran_str + type
         destination = open(dir + fname, 'wb+')
         for chunk in myFile.chunks():
            destination.write(chunk)
         destination.close()
         return JsonResponse({'msg': 'ok','fname': fname})
      else:
         return JsonResponse({'msg': 'erroe'})


@csrf_exempt
def Cartridge_update(request):
   try:
      if request.method == "POST":
         result = simplejson.loads(request.body)
         if result["PWD"] == "%^*IFGbgi2332322253gr":
            xx = models.Cartridge.objects.get(id=result["id"])
            xx.number = result["num"]
            xx.save()
            return HttpResponse("ok")
         else:
            return HttpResponse("password")
   except Exception as e:
      return HttpResponse(str(e))
# endregion
