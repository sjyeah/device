# Generated by Django 3.0.5 on 2020-05-10 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('htgl', '0003_auto_20200510_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='depid',
            field=models.ForeignKey(db_column='depID', null=True, on_delete=django.db.models.deletion.PROTECT, to='htgl.department', verbose_name='责任处室'),
        ),
        migrations.AddField(
            model_name='device',
            name='memid',
            field=models.ForeignKey(db_column='memID', null=True, on_delete=django.db.models.deletion.PROTECT, to='htgl.member', verbose_name='责任人'),
        ),
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.DateField(blank=True, null=True, verbose_name='房间号'),
        ),
        migrations.AlterField(
            model_name='device',
            name='brand',
            field=models.CharField(blank=True, editable=False, max_length=10, null=True, verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.CharField(max_length=50, verbose_name='品牌和型号'),
        ),
    ]
