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
      verbose_name = '硒鼓'
      verbose_name_plural = verbose_name

   def __str__(self):
      data = self.model + '(' + self.color + ')'
      return data


class sys(models.Model):
   codename = models.CharField(db_column='codeName', max_length=20, blank=True, null=True, verbose_name='名称')
   sort = models.IntegerField(blank=True, null=True, verbose_name='排序')
   type = models.IntegerField(blank=True, null=True, verbose_name='代码类别',
                              choices=((1, '设备类别'), (2, '设备状态'), (3, '设备审批'), (4, '借用状态'),
                                       (5, '负责人'), (6, '进度'), (7, '模块')))

   class Meta:
      managed = True
      db_table = 'sys'
      verbose_name = '代码'
      verbose_name_plural = verbose_name

   def __str__(self):
      return self.codename


class department(models.Model):
   depname = models.CharField(db_column='depName', max_length=20, blank=True, null=True, verbose_name='名称')
   dingid = models.CharField(db_column='dingID', max_length=20, blank=True, null=True, unique=True, verbose_name='dingID')
   sort = models.IntegerField(blank=True, null=True, verbose_name='排序')

   class Meta:
      managed = True
      db_table = 'department'
      verbose_name = '部门'
      verbose_name_plural = verbose_name

   def __str__(self):
      return self.depname


class member(models.Model):
   dingid = models.CharField(db_column='dingID', max_length=20, blank=True, null=True, unique=True, verbose_name='钉钉编号')
   name = models.CharField(db_column='memberName', max_length=10, blank=False, null=False, verbose_name='姓名')
   sort = models.IntegerField(blank=True, null=True, verbose_name='排序')
   depid = models.ForeignKey(department, db_column='depID', to_field='id', null=True, blank=True, verbose_name='所属处室', on_delete=models.PROTECT)

   class Meta:
      managed = True
      db_table = 'member'
      verbose_name = '人员'
      verbose_name_plural = verbose_name

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
   updatetime = models.DateTimeField(blank=True, null=True, auto_now=True)

   class Meta:
      managed = True
      db_table = 'device'
      verbose_name = '设备管理'
      verbose_name_plural = '设备'

   def __str__(self):
      return self.model


class RecordBorrow(models.Model):
   userid = models.ForeignKey(member, to_field='dingid', db_column='userid', null=True, on_delete=models.PROTECT, verbose_name='申请人')
   depid = models.ForeignKey(department, db_column='depID', to_field='dingid', null=True, verbose_name='申请处室', on_delete=models.PROTECT)
   devices = models.ManyToManyField(Device, verbose_name='借用设备')
   etime = models.DateField(blank=True, null=True, verbose_name='归还时间')
   stime = models.DateField(blank=True, null=True, verbose_name='借用时间')
   reason = models.CharField(max_length=500, blank=True, null=True, verbose_name='借用原因')
   memo = models.CharField(max_length=200, blank=True, null=True, verbose_name='备注')
   status = models.ForeignKey(sys, db_column='status', blank=True, null=True, related_name='jyzt', to_field='id', limit_choices_to={'type': '3'},
                              verbose_name='状态', on_delete=models.PROTECT)
   recordtime = models.DateTimeField(auto_now_add=True, verbose_name='生成时间', null=True, editable=False)
   updatetime = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, editable=False)

   class Meta:
      managed = True
      db_table = 'record_borrow'
      verbose_name = '设备借用'
      verbose_name_plural = verbose_name


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
      verbose_name_plural = verbose_name


class RecordDevice(models.Model):
   did = models.ForeignKey(Device, db_column='dID', to_field='id', null=True, on_delete=models.PROTECT, verbose_name='设备id')
   borrowid = models.ForeignKey(RecordBorrow, db_column='borrowID', to_field='id', on_delete=models.PROTECT, null=True, verbose_name='借用id')
   returntime = models.DateField(blank=True, null=True, verbose_name='归还时间')
   status = models.ForeignKey(sys, db_column='status', blank=True, null=True, related_name='ghzt', to_field='id', limit_choices_to={'type': '4'},
                              verbose_name='状态', on_delete=models.PROTECT)
   recordtime = models.DateTimeField(null=True, auto_now_add=True)
   updatetime = models.DateTimeField(null=True, auto_now=True)

   class Meta:
      managed = True
      db_table = 'record_device'
      verbose_name = '借用记录'
      verbose_name_plural = verbose_name
      unique_together = (('did', 'borrowid'),)


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
   os = models.CharField(max_length=50, blank=False, null=False, verbose_name='操作系统', default='Windows Server 2008 R2')
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


class xuqiu(models.Model):
   title = models.ForeignKey(sys, db_column='title',related_name='r2', to_field='id', limit_choices_to={'type': '7'}, verbose_name='模块', on_delete=models.PROTECT)
   content = models.TextField(max_length=500, blank=True, null=True, verbose_name='描述')
   feedbacktime = models.DateField(verbose_name='反馈时间',null=True,blank=True)
   plantime = models.DateField(verbose_name='计划完成时间',null=True,blank=True)
   manager = models.ForeignKey(sys, db_column='manager',null=True,blank=True, related_name='r3',to_field='id', limit_choices_to={'type': '5'}, verbose_name='负责人', on_delete=models.PROTECT)
   zt = models.ForeignKey(sys, db_column='zt',related_name='r1',null=True,blank=True, to_field='id', limit_choices_to={'type': '6'}, verbose_name='状态', on_delete=models.PROTECT)
   memo = models.IntegerField(null=False, blank=False, choices=((0, '未完成'), (1, '完成')), default=0, verbose_name='项目经理测试')
   recordtime = models.DateTimeField(blank=True, null=True, auto_now_add=True)
   updatetime = models.DateTimeField(blank=True, null=True, auto_now=True)
   sort = models.IntegerField(default=99, verbose_name='排序')

   class Meta:
      managed = True
      db_table = 'xuqiu'
      verbose_name = '需求和BUG'
      verbose_name_plural = verbose_name
      sorted('sort')
