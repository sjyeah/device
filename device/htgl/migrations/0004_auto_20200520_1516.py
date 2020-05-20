# Generated by Django 3.0.5 on 2020-05-20 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('htgl', '0003_auto_20200520_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordborrow',
            name='status',
            field=models.ForeignKey(blank=True, db_column='status', default=15, limit_choices_to={'type': '3'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jyzt', to='htgl.sys', verbose_name='状态'),
        ),
    ]
