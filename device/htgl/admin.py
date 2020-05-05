from django.contrib import admin
from .models import Cartridge,Device,Printer

admin.site.site_header = '设备管理后台'
admin.site.site_title = '设备管理'
# Register your models here.
class CartridgeAdmin(admin.ModelAdmin):
    list_display = ['id','model','brand','number','color']
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 10
admin.site.register(Cartridge,CartridgeAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id','model','brand','pic','sn','buytime','type']
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 10



admin.site.register(Device, DeviceAdmin)


class PrinterAdmin(admin.ModelAdmin):
    list_display = ['id','model','brand','pic','cartridges']
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 10


admin.site.register(Printer, PrinterAdmin)

