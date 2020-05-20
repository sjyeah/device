# Generated by Django 3.0.5 on 2020-05-20 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('htgl', '0005_auto_20200520_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sys',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '设备类别'), (2, '设备状态'), (3, '设备审批'), (4, '借用状态'), (5, '负责人'), (6, '进度'), (7, '模块')], null=True, verbose_name='代码类别'),
        ),
        migrations.CreateModel(
            name='xuqiu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedbacktime', models.DateField(verbose_name='反馈时间')),
                ('plantime', models.DateField(verbose_name='计划完成时间')),
                ('memo', models.IntegerField(choices=[(0, '未完成'), (1, '完成')], default=0, verbose_name='项目经理测试')),
                ('recordtime', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True, null=True)),
                ('sort', models.IntegerField(default=99, verbose_name='排序')),
                ('manager', models.ForeignKey(db_column='manager', limit_choices_to={'type': '5'}, on_delete=django.db.models.deletion.PROTECT, related_name='r3', to='htgl.sys', verbose_name='负责人')),
                ('title', models.ForeignKey(db_column='title', limit_choices_to={'type': '7'}, on_delete=django.db.models.deletion.PROTECT, related_name='r2', to='htgl.sys', verbose_name='模块')),
                ('zt', models.ForeignKey(db_column='zt', limit_choices_to={'type': '6'}, on_delete=django.db.models.deletion.PROTECT, related_name='r1', to='htgl.sys', verbose_name='状态')),
            ],
            options={
                'verbose_name': '需求和BUG',
                'verbose_name_plural': '需求和BUG',
                'db_table': 'xuqiu',
                'managed': True,
            },
        ),
    ]
