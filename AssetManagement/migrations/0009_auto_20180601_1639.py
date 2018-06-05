# Generated by Django 2.0.5 on 2018-06-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0008_remove_hostinfo_hostgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='Jumpserver',
            field=models.CharField(max_length=32, verbose_name='是否加入堡垒机'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='Keepass',
            field=models.CharField(max_length=32, verbose_name='是否记录密码'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='Salt',
            field=models.CharField(max_length=32, verbose_name='是否加入自动化运维'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='Zabbix',
            field=models.CharField(max_length=32, verbose_name='是否加入监控'),
        ),
    ]