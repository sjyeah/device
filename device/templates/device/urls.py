from django.conf.urls import url
from htgl import views

urlpatterns = [
    url(r'^list/$', views.devicelist)
]