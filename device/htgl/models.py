from django.db import models

# Create your models here.


class BorrowDetail(models.Model):
    did = models.IntegerField(db_column='dID', blank=True, null=True)  # Field name made lowercase.
    bid = models.IntegerField(db_column='bID', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borrow_detail'


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


class sys(models.Model):
    typename = models.CharField(max_length=20, blank=True, null=True)
    sort= models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys'

    def __str__(self):
        return self.typename


class Device(models.Model):
            model = models.CharField(max_length=50, blank=True, null=True, verbose_name='型号')
            brand = models.CharField(max_length=10, blank=True, null=True, verbose_name='品牌')
            pic = models.CharField(max_length=100, blank=True, null=True, verbose_name='图片')
            sn = models.CharField(max_length=50, blank=True, null=True, verbose_name='序列号')
            type = models.ForeignKey(sys, db_column='type',to_field='id',null=True, verbose_name='类别',on_delete=models.DO_NOTHING)
            buytime = models.CharField(db_column='buyTime', max_length=50, blank=True,
                                       null=True, verbose_name='购置时间')  # Field name made lowercase.
            memo = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')
            status = models.CharField(max_length=1, blank=True, null=True)
            recordtime = models.DateTimeField(blank=True, null=True)

            class Meta:
                managed = True
                db_table = 'device'
                verbose_name = '设备'
                verbose_name_plural = '设备列表'


class Printer(models.Model):
                    model = models.CharField(max_length=50, blank=True, null=True, verbose_name='型号')
                    brand = models.CharField(max_length=10, blank=True, null=True, verbose_name='品牌')
                    pic = models.CharField(max_length=100, blank=True, null=True)
                    cartridges = models.CharField(max_length=50, blank=True, null=True, verbose_name='使用的硒鼓')

                    class Meta:
                        managed = True
                        db_table = 'printer'
                        verbose_name = '打印机种类'
                        verbose_name_plural = '打印机种类列表'

class RecordApply(models.Model):
                    userid = models.CharField(max_length=20, blank=True, null=True)
                    username = models.CharField(max_length=20, blank=True, null=True)
                    deptid = models.CharField(db_column='deptID', max_length=20, blank=True,
                                              null=True)  # Field name made lowercase.
                    department = models.CharField(max_length=20, blank=True, null=True)
                    recordtime = models.DateTimeField(blank=True, null=True)
                    amount = models.IntegerField(blank=True, null=True)
                    crid = models.IntegerField(db_column='crID')  # Field name made lowercase.
                    ctime = models.DateTimeField(blank=True, null=True)
                    memo = models.CharField(max_length=200, blank=True, null=True)

                    class Meta:
                        managed = False
                        db_table = 'record_apply'

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

class RecordBorrow(models.Model):
                    userid = models.CharField(max_length=20, blank=True, null=True)
                    username = models.CharField(max_length=20, blank=True, null=True)
                    deptid = models.CharField(db_column='deptID', max_length=20, blank=True,
                                              null=True)  # Field name made lowercase.
                    department = models.CharField(max_length=50, blank=True, null=True)
                    devices = models.CharField(max_length=500, blank=True, null=True)
                    etime = models.CharField(max_length=10, blank=True, null=True)
                    stime = models.CharField(max_length=10, blank=True, null=True)
                    reason = models.CharField(max_length=500, blank=True, null=True)
                    memo = models.CharField(max_length=200, blank=True, null=True)
                    status = models.CharField(max_length=1, blank=True, null=True)
                    recordtime = models.DateTimeField(blank=True, null=True)

                    class Meta:
                        managed = False
                        db_table = 'record_borrow'

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


