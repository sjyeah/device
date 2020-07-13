# Generated by Django 3.0.5 on 2020-05-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htgl', '0004_auto_20200516_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecs',
            name='ip',
            field=models.CharField(max_length=15, unique=True, verbose_name='内网IP'),
        ),
        migrations.AlterField(
            model_name='ecs',
            name='os',
            field=models.CharField(default='CentOS 7.4 64位', max_length=30, verbose_name='操作系统'),
        ),
        migrations.AlterField(
            model_name='ecs',
            name='sn',
            field=models.CharField(max_length=50, unique=True, verbose_name='实例id'),
        ),
    ]