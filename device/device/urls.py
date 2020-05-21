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
from django.urls import path
from django.conf.urls import url
from htgl import views

urlpatterns = [
   # path('admin/', views.index),
   url(r'^admin/', admin.site.urls),
   path('login/', views.login_user),
   path('logout/', views.logout),
   path('device/audit/', views.borrowAudit),
   path('device/disagree/<int:id>', views.borrowAudit2),
   # path('device/<int:id>', views.deviceDetail),
   # path('device/delete/<int:id>', views.deviceDelete),
   # path('device/update/<intid>', views.deviceUpdate),
   # path('device/add/', views.deviceAdd),
   path('device/', views.borrowList),
   # path('cartridge/', views.cartridgeList),
   # path('cartridge/detail/<int:id>', views.cartridgeDetail),
   # path('cartridge/update/<int:id>', views.cartridgeUpdate),
   # path('cartridge/delete/<int:id>', views.cartridgeDelete),
   # path('cartridge/add/', views.cartridgeAdd)

   # url(r'^device/', views.deviceList),
   path('', views.index),
   path('index/', views.index)

]
