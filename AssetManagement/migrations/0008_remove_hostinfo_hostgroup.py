# Generated by Django 2.0.5 on 2018-06-01 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0007_hostandhgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostinfo',
            name='HostGroup',
        ),
    ]
