from django.contrib import admin
from .models import Cartridge, Device, Printer, sys, RecordApply

admin.site.site_header = '设备管理后台'
admin.site.site_title = '设备管理'


# Register your models here.
class sysAdmin(admin.ModelAdmin):
    list_display = ['id', 'typename', 'sort']
    list_per_page = 20


admin.site.register(sys, sysAdmin)


class CartridgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'brand', 'number', 'color']
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 20


admin.site.register(Cartridge, CartridgeAdmin)


class RecordApplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'crid', 'amount', 'username','department','recordtime']
    list_filter = ['username','department','crid']
    search_fields = ['username','department']
    list_per_page = 20


admin.site.register(RecordApply, RecordApplyAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'brand', 'pic', 'sn', 'buytime', 'type']
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 20


admin.site.register(Device, DeviceAdmin)


class PrinterAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'brand', 'pic', 'cartridges']
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 20


admin.site.register(Printer, PrinterAdmin)
