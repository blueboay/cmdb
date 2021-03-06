# Generated by Django 2.0.5 on 2018-08-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0022_auto_20180813_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkdevice',
            name='ConsoleUser',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Console管理用户名'),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='ManageIP',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='SSH远程管理IP'),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='ManageUser',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='SSH远程管理用户'),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='Password',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='SSH远程密码'),
        ),
    ]
