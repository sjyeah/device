from django.contrib import admin
from .models import Device, Printer, sys, RecordApply, Cartridge,RecordBorrow

admin.site.site_header = '设备管理后台'
admin.site.site_title = '设备管理'


# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'depid', 'memid', 'room','buytime', 'type']
    list_filter = ['type']
    search_fields = ['model']
    list_per_page = 20
    change_form_template = 'device/detail.html'


class sysAdmin(admin.ModelAdmin):
    list_display = ['id', 'codename', 'sort']
    list_per_page = 20


class CartridgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'brand', 'number', 'color']
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 20


class RecordApplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'crid', 'amount', 'username', 'department', 'recordtime']
    list_filter = ['department', 'crid']
    search_fields = ['username']
    list_per_page = 20


class RecordBorrowAdmin(admin.ModelAdmin):
    list_display = ['id', 'reason', 'stime', 'etime', 'devices', 'username', 'department', 'recordtime']
    list_filter = ['department', 'username']
    search_fields = ['username']
    list_per_page = 20


class PrinterAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'brand', 'pic', 'cartridges']
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 20


admin.site.register(Printer, PrinterAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(sys, sysAdmin)
admin.site.register(RecordApply, RecordApplyAdmin)
admin.site.register(Cartridge, CartridgeAdmin)
admin.site.register(RecordBorrow, RecordBorrowAdmin)
