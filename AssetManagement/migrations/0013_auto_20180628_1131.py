# Generated by Django 2.0.5 on 2018-06-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0012_networkdevice_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostinfo',
            name='Brand',
            field=models.CharField(blank=True, max_length=32, verbose_name='品牌'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='Owner',
            field=models.CharField(blank=True, max_length=32, verbose_name='所有者'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='Position',
            field=models.CharField(blank=True, max_length=32, verbose_name='位置'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='ServerType',
            field=models.CharField(blank=True, max_length=32, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='PhoneNumber',
            field=models.IntegerField(blank=True, null=True, verbose_name='手机'),
        ),
    ]
