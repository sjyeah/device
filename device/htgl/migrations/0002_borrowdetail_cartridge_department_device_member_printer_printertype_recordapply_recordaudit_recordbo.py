# Generated by Django 3.0.5 on 2020-05-16 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('htgl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.IntegerField(blank=True, db_column='dID', null=True)),
                ('bid', models.IntegerField(blank=True, db_column='bID', null=True)),
                ('recordtime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '借用详细',
                'verbose_name_plural': '借用详细',
                'db_table': 'borrow_detail',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cartridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20, verbose_name='型号')),
                ('color', models.CharField(blank=True, max_length=5, null=True, verbose_name='颜色')),
                ('code', models.CharField(blank=True, max_length=4, null=True)),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='数量')),
                ('brand', models.CharField(blank=True, max_length=20, null=True, verbose_name='品牌')),
            ],
            options={
                'verbose_name': '硒鼓管理',
                'verbose_name_plural': '硒鼓管理',
                'db_table': 'cartridge',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depname', models.CharField(blank=True, db_column='depName', max_length=20, null=True, verbose_name='名称')),
                ('sort', models.IntegerField(blank=True, null=True, verbose_name='排序')),
            ],
            options={
                'verbose_name': '部门管理',
                'verbose_name_plural': '部门',
                'db_table': 'department',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=50, null=True, verbose_name='型号')),
                ('brand', models.CharField(blank=True, max_length=10, null=True, verbose_name='品牌')),
                ('pic', models.CharField(blank=True, max_length=100, null=True)),
                ('cartridges', models.CharField(blank=True, max_length=50, null=True, verbose_name='使用的硒鼓')),
            ],
            options={
                'verbose_name': '打印机型号',
                'verbose_name_plural': '型号',
                'db_table': 'printer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RecordAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField(blank=True, db_column='bID', null=True)),
                ('parentid', models.IntegerField(blank=True, db_column='parentID', null=True)),
                ('username', models.CharField(blank=True, max_length=10, null=True)),
                ('userid', models.CharField(blank=True, max_length=20, null=True)),
                ('memo', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('recordtime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '借用审批记录',
                'verbose_name_plural': '借用审批记录',
                'db_table': 'record_audit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RecordBorrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人')),
                ('deptid', models.CharField(blank=True, db_column='deptID', max_length=20, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True, verbose_name='申请人部门')),
                ('devices', models.CharField(blank=True, max_length=500, null=True, verbose_name='设备列表')),
                ('etime', models.DateField(blank=True, null=True, verbose_name='归还时间')),
                ('stime', models.DateField(blank=True, null=True, verbose_name='借用时间')),
                ('reason', models.CharField(blank=True, max_length=500, null=True, verbose_name='借用原因')),
                ('memo', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('status', models.CharField(blank=True, max_length=1, null=True, verbose_name='型号')),
                ('recordtime', models.DateTimeField(blank=True, null=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '设备借用申请',
                'verbose_name_plural': '设备借用申请',
                'db_table': 'record_borrow',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RecordDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('deptid', models.CharField(blank=True, db_column='deptID', max_length=20, null=True)),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('recordtime', models.DateTimeField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('did', models.IntegerField(blank=True, db_column='dID', null=True)),
                ('ctime', models.DateTimeField(blank=True, null=True)),
                ('rtime', models.DateField(blank=True, null=True)),
                ('memo', models.CharField(blank=True, max_length=200, null=True)),
                ('stime', models.DateField(blank=True, db_column='sTime', null=True)),
                ('etime', models.DateField(blank=True, db_column='eTime', null=True)),
                ('return_field', models.CharField(blank=True, db_column='return', max_length=1, null=True)),
            ],
            options={
                'verbose_name': '借用记录',
                'verbose_name_plural': '借用记录',
                'db_table': 'record_device',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='sys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(blank=True, db_column='codeName', max_length=20, null=True, verbose_name='名称')),
                ('sort', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('type', models.IntegerField(blank=True, choices=[(1, '设备类别'), (2, '设备状态')], null=True, verbose_name='代码类别')),
            ],
            options={
                'verbose_name': '设备类别',
                'verbose_name_plural': '设备类别',
                'db_table': 'sys',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RecordApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True, verbose_name='申领人')),
                ('deptid', models.CharField(blank=True, db_column='deptID', max_length=20, null=True)),
                ('department', models.CharField(blank=True, max_length=20, null=True, verbose_name='申领部门')),
                ('recordtime', models.DateTimeField(blank=True, null=True, verbose_name='申领时间')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='数量')),
                ('ctime', models.DateTimeField(blank=True, null=True, verbose_name='确认时间')),
                ('memo', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('crid', models.ForeignKey(db_column='crID', null=True, on_delete=django.db.models.deletion.PROTECT, to='htgl.Cartridge', verbose_name='申领耗材')),
            ],
            options={
                'verbose_name': '耗材申领记录',
                'verbose_name_plural': '耗材申领记录',
                'db_table': 'record_apply',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PrinterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=50, null=True, verbose_name='型号')),
                ('brand', models.CharField(blank=True, max_length=10, null=True, verbose_name='品牌')),
                ('pic', models.CharField(blank=True, max_length=100, null=True)),
                ('cartridges', models.ManyToManyField(to='htgl.Cartridge', verbose_name='使用的硒鼓')),
            ],
            options={
                'verbose_name': '打印机型号',
                'verbose_name_plural': '型号',
                'db_table': 'printertype',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='memberName', max_length=10, verbose_name='姓名')),
                ('sort', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('depid', models.ForeignKey(blank=True, db_column='depID', null=True, on_delete=django.db.models.deletion.PROTECT, to='htgl.department', verbose_name='所属处室')),
            ],
            options={
                'verbose_name': '成员管理',
                'verbose_name_plural': '成员',
                'db_table': 'member',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='品牌和型号')),
                ('brand', models.CharField(blank=True, editable=False, max_length=10, null=True, verbose_name='品牌')),
                ('pic', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='图片')),
                ('sn', models.CharField(blank=True, max_length=50, null=True, verbose_name='序列号')),
                ('room', models.CharField(blank=True, max_length=20, null=True, verbose_name='房间号')),
                ('buytime', models.DateField(blank=True, db_column='buyTime', null=True, verbose_name='购置时间')),
                ('memo', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('recordtime', models.DateTimeField(auto_now_add=True, null=True)),
                ('depid', models.ForeignKey(db_column='depID', null=True, on_delete=django.db.models.deletion.PROTECT, to='htgl.department', verbose_name='责任处室')),
                ('memid', models.ForeignKey(db_column='memID', null=True, on_delete=django.db.models.deletion.PROTECT, to='htgl.member', verbose_name='责任人')),
                ('status', models.ForeignKey(blank=True, db_column='status', limit_choices_to={'type': '2'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='zt', to='htgl.sys', verbose_name='状态')),
                ('type', models.ForeignKey(db_column='type', limit_choices_to={'type': '1'}, null=True, on_delete=django.db.models.deletion.PROTECT, to='htgl.sys', verbose_name='类别')),
            ],
            options={
                'verbose_name': '设备管理',
                'verbose_name_plural': '设备',
                'db_table': 'device',
                'managed': True,
            },
        ),
    ]
