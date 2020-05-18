from django.contrib import admin
from .models import Device, Printer, sys, RecordApply, Cartridge, RecordBorrow, department, member, PrinterType, ecs, ecsstatus

admin.site.site_header = '设备管理后台'
admin.site.site_title = '设备管理'


# Register your models here.
class typeFilter(admin.SimpleListFilter):
    title = ('设备类别')
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        dlist = sys.objects.filter(type=1).order_by('sort').values_list('codename', 'id')
        data = []
        for name, id in dlist:
            temp = (id, name)
            data.append(temp)
        return data

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(type=self.value())
        else:
            return queryset.all()


class depFilter(admin.SimpleListFilter):
    title = ('责任处室')
    parameter_name = 'depid'

    def lookups(self, request, model_admin):
        dlist = department.objects.all().order_by('sort').values_list('depname', 'id')
        data = []
        for name, id in dlist:
            temp = (id, name)
            data.append(temp)
        return data

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(depid=self.value())
        else:
            return queryset.all()


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'depid', 'memid', 'room', 'status', 'type']
    # list_filter =['type']
    list_filter = (typeFilter, depFilter,)
    search_fields = ['model']
    list_per_page = 20
    change_form_template = 'device/edit.html'
    ordering = ('type', 'depid')


class sysAdmin(admin.ModelAdmin):
    list_display = ['id', 'codename', 'sort', 'type']
    list_per_page = 20
    ordering = ('sort',)


class memberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'depid', 'sort']
    list_filter = (depFilter,)
    search_fields = ['name']
    list_per_page = 20
    ordering = ('depid', 'sort',)


class departmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'depname', 'sort']
    search_fields = ['depname']
    list_per_page = 20
    ordering = ('sort',)


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
    def 借用的设备(self):
        return [a.model for a in self.devices.all()]
    list_display = ['id', 'reason', 'stime', 'etime', 借用的设备, 'userid', 'depid']
    list_filter = ['depid']
    search_fields = ['userid']
    list_per_page = 20


class PrinterAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'brand', 'cartridges']
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 20


class PrintertypeAdmin(admin.ModelAdmin):
    def 使用的硒鼓(self):
        return [a.model + '(' + a.color + ')' for a in self.cartridges.all()]

    list_display = ['id', 'model', 'brand', 'pic', 使用的硒鼓]
    list_filter = ['model']
    search_fields = ['model']
    list_per_page = 20


class ecsstatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 20


class ecsAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'internetip', 'os', 'net', 'cpu', 'ram', 'disk', 'status']
    list_filter = ['status', 'net', 'cpu']
    search_fields = ['ip']


admin.site.register(ecs, ecsAdmin)
admin.site.register(ecsstatus, ecsstatusAdmin)
admin.site.register(Printer, PrinterAdmin)
admin.site.register(PrinterType, PrintertypeAdmin)
admin.site.register(department, departmentAdmin)
admin.site.register(member, memberAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(sys, sysAdmin)
admin.site.register(RecordApply, RecordApplyAdmin)
admin.site.register(Cartridge, CartridgeAdmin)
admin.site.register(RecordBorrow, RecordBorrowAdmin)
