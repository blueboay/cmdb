# Generated by Django 2.0.5 on 2018-06-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0010_auto_20180601_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostAndHGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServerName', models.CharField(max_length=32, verbose_name='服务器名称')),
                ('GroupName', models.CharField(max_length=32, verbose_name='分组名称')),
            ],
        ),
        migrations.RemoveField(
            model_name='hostgroup',
            name='GroupName',
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='GroupName',
            field=models.CharField(default='', max_length=32, verbose_name='分组名称'),
        ),
    ]
