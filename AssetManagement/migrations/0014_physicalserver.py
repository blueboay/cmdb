# Generated by Django 2.0.5 on 2018-07-02 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0013_auto_20180628_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicalServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(max_length=32, verbose_name='型号')),
                ('Type', models.CharField(max_length=32, verbose_name='类型')),
                ('SN', models.CharField(max_length=32, verbose_name='序列号')),
                ('Brand', models.CharField(max_length=32, verbose_name='品牌')),
                ('Position', models.CharField(max_length=32, verbose_name='位置')),
                ('ManageIP', models.CharField(blank=True, max_length=32, null=True, verbose_name='管理IP')),
                ('ManageUsername', models.CharField(blank=True, max_length=32, null=True, verbose_name='管理用户名')),
                ('ManagePassword', models.CharField(blank=True, max_length=32, null=True, verbose_name='管理密码')),
                ('ExpireData', models.CharField(max_length=32, verbose_name='维保过期时间')),
                ('CPU', models.CharField(max_length=32, verbose_name='型号')),
                ('Memory', models.CharField(max_length=32, verbose_name='型号')),
                ('TotalSpace', models.CharField(max_length=32, verbose_name='总空间')),
            ],
        ),
    ]
