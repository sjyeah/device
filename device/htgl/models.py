from django.db import models


# Create your models here.


class Cartridge(models.Model):
    model = models.CharField(max_length=20, blank=True, null=True, verbose_name='型号')
    color = models.CharField(max_length=5, blank=True, null=True, verbose_name='颜色')
    code = models.CharField(max_length=4, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True, verbose_name='数量')
    brand = models.CharField(max_length=20, blank=True, null=True, verbose_name='品牌')

    class Meta:
        managed = False
        db_table = 'cartridge'
        verbose_name = '硒鼓'
        verbose_name_plural = '硒鼓列表'

        def __str__(self):
            return self.model


class sys(models.Model):
    typename = models.CharField(max_length=20, blank=True, null=True, verbose_name='类别名称')
    sort = models.IntegerField(blank=True, null=True, verbose_name='排序')

    class Meta:
        managed = False
        db_table = 'sys'
        verbose_name = '设备类别'
        verbose_name_plural = '设备类别'

    def __str__(self):
        return self.typename


class Printer(models.Model):
    model = models.CharField(max_length=50, blank=True, null=True, verbose_name='型号')
    brand = models.CharField(max_length=10, blank=True, null=True, verbose_name='品牌')
    pic = models.CharField(max_length=100, blank=True, null=True)
    cartridges = models.CharField(max_length=50, blank=True, null=True, verbose_name='使用的硒鼓')

    class Meta:
        managed = False
        db_table = 'printer'
        verbose_name = '打印机种类'
        verbose_name_plural = '打印机种类'


class Device(models.Model):
    model = models.CharField(max_length=50, blank=True, null=True, verbose_name='型号')
    brand = models.CharField(max_length=10, blank=True, null=True, verbose_name='品牌')
    pic = models.CharField(max_length=100, blank=True, null=True, verbose_name='图片')
    sn = models.CharField(max_length=50, blank=True, null=True, verbose_name='序列号')
    type = models.ForeignKey(sys, db_column='type', to_field='id', null=True, verbose_name='类别',
                             on_delete=models.PROTECT)
    buytime = models.CharField(db_column='buyTime', max_length=50, blank=True,
                               null=True, verbose_name='购置时间')  # Field name made lowercase.
    memo = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')
    status = models.CharField(max_length=1, blank=True, null=True)
    recordtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'
        verbose_name = '设备'
        verbose_name_plural = '设备列表'


class RecordBorrow(models.Model):
    userid = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True, verbose_name='申请人')
    deptid = models.CharField(db_column='deptID', max_length=20, blank=True,
                              null=True)  # Field name made lowercase.
    department = models.CharField(max_length=50, blank=True, null=True, verbose_name='申请人部门')
    devices = models.CharField(max_length=500, blank=True, null=True, verbose_name='设备列表')
    etime = models.CharField(max_length=10, blank=True, null=True, verbose_name='归还时间')
    stime = models.CharField(max_length=10, blank=True, null=True, verbose_name='借用时间')
    reason = models.CharField(max_length=500, blank=True, null=True, verbose_name='借用原因')
    memo = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')
    status = models.CharField(max_length=1, blank=True, null=True, verbose_name='型号')
    recordtime = models.DateTimeField(blank=True, null=True, verbose_name='状态')

    class Meta:
        managed = False
        db_table = 'record_borrow'
        verbose_name = '设备借用申请'
        verbose_name_plural = '设备借用申请'


class BorrowDetail(models.Model):
    did = models.IntegerField(db_column='dID', blank=True, null=True)  # Field name made lowercase.
    bid = models.IntegerField(db_column='bID', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borrow_detail'
        verbose_name = '借用详细'
        verbose_name_plural = '借用详细'


class RecordApply(models.Model):
    userid = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True, verbose_name='申领人')
    deptid = models.CharField(db_column='deptID', max_length=20, blank=True,
                              null=True)  # Field name made lowercase.
    department = models.CharField(max_length=20, blank=True, null=True, verbose_name='申领部门')
    recordtime = models.DateTimeField(blank=True, null=True, verbose_name='申领时间')
    amount = models.IntegerField(blank=True, null=True, verbose_name='数量')
    crid = models.ForeignKey(Cartridge, db_column='crID', to_field='id', null=True,on_delete=models.PROTECT, verbose_name='申领耗材')  # Field name made lowercase.
    ctime = models.DateTimeField(blank=True, null=True, verbose_name='确认时间')
    memo = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

    class Meta:
        managed = False
        db_table = 'record_apply'
        verbose_name = '耗材记录'
        verbose_name_plural = '耗材记录'


class RecordAudit(models.Model):
    bid = models.IntegerField(db_column='bID', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentID', blank=True,
                                   null=True)  # Field name made lowercase.
    username = models.CharField(max_length=10, blank=True, null=True)
    userid = models.CharField(max_length=20, blank=True, null=True)
    memo = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    recordtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_audit'
        verbose_name = '借用审批'
        verbose_name_plural = '借用审批'


class RecordDevice(models.Model):
    userid = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    deptid = models.CharField(db_column='deptID', max_length=20, blank=True,
                              null=True)  # Field name made lowercase.
    department = models.CharField(max_length=20, blank=True, null=True)
    recordtime = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    did = models.IntegerField(db_column='dID', blank=True, null=True)  # Field name made lowercase.
    ctime = models.DateTimeField(blank=True, null=True)
    rtime = models.CharField(max_length=20, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    stime = models.CharField(db_column='sTime', max_length=20, blank=True,
                             null=True)  # Field name made lowercase.
    etime = models.CharField(db_column='eTime', max_length=20, blank=True,
                             null=True)  # Field name made lowercase.
    return_field = models.CharField(db_column='return', max_length=1, blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'record_device'
        verbose_name = '借用记录'
        verbose_name_plural = '借用记录'
