from django.db import models, reset_queries


# Create your models here.


class Cartridge(models.Model):
   model = models.CharField(max_length=20, blank=False, null=False, verbose_name='型号')
   color = models.CharField(max_length=5, blank=True, null=True, verbose_name='颜色')
   code = models.CharField(max_length=4, blank=True, null=True)
   number = models.IntegerField(blank=True, null=True, verbose_name='数量')
   brand = models.CharField(max_length=20, blank=True, null=True, verbose_name='品牌')

   class Meta:
      managed = True
      db_table = 'cartridge'
      verbose_name = '硒鼓管理'
      verbose_name_plural = '硒鼓管理'

   def __str__(self):
      data = self.model + '(' + self.color + ')'
      return data


class sys(models.Model):
   codename = models.CharField(db_column='codeName', max_length=20, blank=True, null=True, verbose_name='名称')
   sort = models.IntegerField(blank=True, null=True, verbose_name='排序')
   type = models.IntegerField(blank=True, null=True, verbose_name='代码类别', choices=((1, '设备类别'), (2, '设备状态')))

   class Meta:
      managed = True
      db_table = 'sys'
      verbose_name = '设备类别'
      verbose_name_plural = verbose_name

   def __str__(self):
      return self.codename


class department(models.Model):
   depname = models.CharField(db_column='depName', max_length=20, blank=True, null=True, verbose_name='名称')
   sort = models.IntegerField(blank=True, null=True, verbose_name='排序')

   class Meta:
      managed = True
      db_table = 'department'
      verbose_name = '部门管理'
      verbose_name_plural = '部门'

   def __str__(self):
      return self.depname


class member(models.Model):
   dingID = models.CharField(max_length=20, blank=True, null=True, verbose_name='钉钉编号')
   name = models.CharField(db_column='memberName', max_length=10, blank=False, null=False, verbose_name='姓名')
   sort = models.IntegerField(blank=True, null=True, verbose_name='排序')
   depid = models.ForeignKey(department, db_column='depID', to_field='id', null=True, blank=True, verbose_name='所属处室', on_delete=models.PROTECT)

   class Meta:
      managed = True
      db_table = 'member'
      verbose_name = '成员管理'
      verbose_name_plural = '成员'

   def __str__(self):
       return self.name





class Printer(models.Model):
   model = models.CharField(max_length=50, blank=True, null=True, verbose_name='型号')
   brand = models.CharField(max_length=10, blank=True, null=True, verbose_name='品牌')
   pic = models.CharField(max_length=100, blank=True, null=True)
   cartridges = models.CharField(max_length=50, blank=True, null=True, verbose_name='使用的硒鼓')

   class Meta:
      managed = True
      db_table = 'printer'
      verbose_name = '打印机型号'
      verbose_name_plural = '型号'


class PrinterType(models.Model):
   model = models.CharField(max_length=50, blank=True, null=True, verbose_name='型号')
   brand = models.CharField(max_length=10, blank=True, null=True, verbose_name='品牌')
   pic = models.CharField(max_length=100, blank=True, null=True)
   cartridges = models.ManyToManyField('cartridge', verbose_name='使用的硒鼓')

   class Meta:
      managed = True
      db_table = 'printertype'
      verbose_name = '打印机型号'
      verbose_name_plural = '型号'


class Device(models.Model):
   model = models.CharField(max_length=50, blank=False, null=False, verbose_name='品牌和型号')
   brand = models.CharField(max_length=10, blank=True, null=True, verbose_name='品牌', editable=False)
   pic = models.CharField(max_length=100, blank=True, null=True, verbose_name='图片', editable=False)
   sn = models.CharField(max_length=50, blank=True, null=True, verbose_name='序列号')
   type = models.ForeignKey(sys, db_column='type', to_field='id', null=True, verbose_name='类别', limit_choices_to={'type': '1'},
                            on_delete=models.PROTECT)
   depid = models.ForeignKey(department, db_column='depID', to_field='id', null=True, verbose_name='责任处室', on_delete=models.PROTECT)
   memid = models.ForeignKey(member, db_column='memID', to_field='id', null=True, verbose_name='责任人', on_delete=models.PROTECT)
   room = models.CharField(max_length=20, blank=True, null=True, verbose_name='房间号')
   buytime = models.DateField(db_column='buyTime', blank=True, null=True, verbose_name='购置时间')
   memo = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')
   status = models.ForeignKey(sys, db_column='status', blank=True, null=True, related_name='zt', to_field='id', limit_choices_to={'type': '2'},
                              verbose_name='状态', on_delete=models.PROTECT)
   recordtime = models.DateTimeField(blank=True, null=True, auto_now_add=True)

   class Meta:
      managed = True
      db_table = 'device'
      verbose_name = '设备管理'
      verbose_name_plural = '设备'


class RecordBorrow(models.Model):
   userid = models.ForeignKey(member,to_field='id',db_column='userid', on_delete=models.PROTECT)
   depid = models.ForeignKey(department, db_column='depID', to_field='id', null=True, verbose_name='责任处室', on_delete=models.PROTECT)
   devices = models.ManyToManyField(Device, verbose_name='设备列表')
   etime = models.DateField(blank=True, null=True, verbose_name='归还时间')
   stime = models.DateField(blank=True, null=True, verbose_name='借用时间')
   reason = models.CharField(max_length=500, blank=True, null=True, verbose_name='借用原因')
   memo = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')
   zt = (('0', '待审批'), ('1', '同意'), ('2', '退回'))
   status = models.IntegerField(choices=zt, verbose_name='状态')
   recordtime = models.DateTimeField(auto_now_add=True, verbose_name='生成时间', editable=False)
   updatetime = models.DateTimeField(auto_now=True, verbose_name='更新时间', editable=False)

   class Meta:
      managed = True
      db_table = 'record_borrow'
      verbose_name = '设备借用申请'
      verbose_name_plural = '设备借用申请'


class RecordApply(models.Model):
   userid = models.CharField(max_length=20, blank=True, null=True)
   username = models.CharField(max_length=20, blank=True, null=True, verbose_name='申领人')
   deptid = models.CharField(db_column='deptID', max_length=20, blank=True,
                             null=True)  # Field name made lowercase.
   department = models.CharField(max_length=20, blank=True, null=True, verbose_name='申领部门')
   recordtime = models.DateTimeField(blank=True, null=True, verbose_name='申领时间')
   amount = models.IntegerField(blank=True, null=True, verbose_name='数量')
   crid = models.ForeignKey(Cartridge, db_column='crID', to_field='id', null=True, on_delete=models.PROTECT,
                            verbose_name='申领耗材')  # Field name made lowercase.
   ctime = models.DateTimeField(blank=True, null=True, verbose_name='确认时间')
   memo = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')

   class Meta:
      managed = True
      db_table = 'record_apply'
      verbose_name = '耗材申领记录'
      verbose_name_plural = '耗材申领记录'


class RecordAudit(models.Model):
   bid = models.IntegerField(db_column='bID', blank=True, null=True)
   parentid = models.IntegerField(db_column='parentID', blank=True, null=True)
   username = models.CharField(max_length=10, blank=True, null=True)
   userid = models.CharField(max_length=20, blank=True, null=True)
   memo = models.CharField(max_length=500, blank=True, null=True)
   status = models.CharField(max_length=1, blank=True, null=True)
   recordtime = models.DateTimeField(blank=True, null=True)

   class Meta:
      managed = True
      db_table = 'record_audit'
      verbose_name = '借用审批记录'
      verbose_name_plural = '借用审批记录'


class RecordDevice(models.Model):
   userid = models.CharField(max_length=20, blank=True, null=True)
   deptid = models.CharField(db_column='deptID', max_length=20, blank=True, null=True)
   type = models.IntegerField(blank=True, null=True)
   did = models.IntegerField(db_column='dID', blank=True, null=True)  # Field name made lowercase.
   ctime = models.DateTimeField(blank=True, null=True)
   rtime = models.DateField(blank=True, null=True)
   memo = models.CharField(max_length=200, blank=True, null=True)
   stime = models.DateField(db_column='sTime', blank=True, null=True)  # Field name made lowercase.
   etime = models.DateField(db_column='eTime', blank=True, null=True)  # Field name made lowercase.
   return_field = models.CharField(db_column='return', max_length=1, blank=True, null=True)
   recordtime = models.DateTimeField(auto_now_add=True)
   updatetime = models.DateTimeField(auto_now=True)

   class Meta:
      managed = True
      db_table = 'record_device'
      verbose_name = '借用记录'
      verbose_name_plural = '借用记录'


class ecsstatus(models.Model):
   name = models.CharField(max_length=15, blank=False, null=False, verbose_name='名称')

   class Meta:
      managed = True
      db_table = 'ecsstatus'
      verbose_name = '状态'
      verbose_name_plural = verbose_name
      sorted('id')

   def __str__(self):
      return self.name


class ecs(models.Model):
   ip = models.CharField(max_length=15, blank=False, null=False, verbose_name='内网IP', unique=True)
   internetip = models.CharField(max_length=15, blank=True, null=True, verbose_name='互联网ip')
   os = models.CharField(max_length=50, blank=False, null=False, verbose_name='操作系统', default='Windows Server 2008 R2 企业版 64位中文版')
   sn = models.CharField(max_length=50, blank=False, null=False, unique=True, verbose_name='实例id')
   status = models.ForeignKey(ecsstatus, db_column='status', to_field='id', null=False, verbose_name='状态', on_delete=models.PROTECT, default=1)
   net = models.CharField(max_length=4, null=False, blank=False, choices=(('VPN1', 'VPN1'), ('VPN2', 'VPN2'), ('VPN3', 'VPN3')), default='VPN1')
   group = models.IntegerField(null=False, blank=False, choices=((1, '转塘集群'), (2, '青山湖集群')), default=1)
   cpu = models.CharField(max_length=20, blank=True, null=True, verbose_name='CPU', default='8核')
   ram = models.CharField(max_length=20, blank=True, null=True, verbose_name='内存', default='16G')
   disk = models.CharField(max_length=20, blank=True, null=True, verbose_name='硬盘', default='500G')
   memo = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')
   recordtime = models.DateTimeField(blank=True, null=True, auto_now_add=True)
   updatetime = models.DateTimeField(blank=True, null=True, auto_now=True)
   sort = models.IntegerField(default=99)

   class Meta:
      managed = True
      db_table = 'ecs'
      verbose_name = '云服务器'
      verbose_name_plural = verbose_name
      sorted('sort')
