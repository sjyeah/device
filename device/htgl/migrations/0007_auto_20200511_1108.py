# Generated by Django 3.0.5 on 2020-05-11 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('htgl', '0006_auto_20200511_1028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'managed': True, 'verbose_name': '设备管理', 'verbose_name_plural': '设备'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'managed': True, 'verbose_name': '成员管理', 'verbose_name_plural': '成员'},
        ),
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='htgl.sys', verbose_name='类别'),
        ),
    ]
