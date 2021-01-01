"""device URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from htgl import views
from django.views.generic.base import RedirectView
from django.views.static import serve

urlpatterns = [
   # path('admin/', views.index),
   path("favicon.ico",RedirectView.as_view(url='static/favicon.ico')),
   url(r'^upload/(?P<path>.*)$', serve, {'document_root': 'upload'}),
   url(r'^admin/', admin.site.urls),
   path('login/', views.login_user),
   path('logout/', views.logout),
   path('borrow/audit/', views.borrowAudit),
   path('device/disagree/<int:id>', views.borrowAudit2),
   path('borrow/add/', views.borrowAdd),
   path('borrow/', views.borrowList),
   path('borrow/<int:id>', views.borrowDetail),
   path('borrow/delete/<int:id>', views.borrowDelete),
   path('borrow/edit/<int:id>', views.borrowEdit),
   path('borrow/return/<int:id>', views.borrowReturn),
   path('device/<int:id>', views.deviceDetail),
   path('device/delete/<int:id>', views.deviceDelete),
   path('device/edit/<int:id>', views.deviceEdit),
   path('device/add/', views.deviceAdd),
   path('device/', views.deviceList),
   path('diary/<int:id>', views.diaryDetail),
   path('diary/delete/<int:id>', views.diaryDelete),
   path('diary/edit/<int:id>', views.diaryEdit),
   path('diary/add/', views.diaryAdd),
   path('diary/', views.diaryList),
   path('member/get/', views.memberList),
   path('project/',views.projectList),
   # path('cartridge/', views.cartridgeList),
   # path('cartridge/detail/<int:id>', views.cartridgeDetail),
   # path('cartridge/update/<int:id>', views.cartridgeUpdate),
   # path('cartridge/delete/<int:id>', views.cartridgeDelete),
   # path('cartridge/add/', views.cartridgeAdd)
   # url(r'^device/', views.deviceList),
   path('', views.index),
   path('index/', views.index),
   path('api/people/', views.people_list),
   path('api/people/update/', views.people_update),
   path('api/people/search/', views.people_search),
   path('api/advice/', views.advice_list),
   path('api/advice/add/', views.advice_add),
   path('api/advice/addpic/', views.advice_addpic),
   path('api/advice/edit/', views.advice_edit),
   path('api/advice/detail/', views.advice_detail),
   path('api/advice/delete/', views.advice_delete),
   path('api/Cartridge/update/', views.Cartridge_update),
   path('api/borrow/audit/', views.borrow_audit),
   path('api/borrow/detail/', views.borrow_detail),
   path('api/borrow/add/', views.borrow_add),
   path('api/borrow/list/', views.borrow_list),
   path('api/borrow/auditlist/', views.borrow_auditlist),
   path('api/member/detail/', views.member_detail),
   path('api/dd/getuser/', views.dd_getuser)
   #path('api/advice/delete', views.advice_delete),
]
