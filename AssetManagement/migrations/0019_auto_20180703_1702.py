# Generated by Django 2.0.5 on 2018-07-03 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0018_auto_20180702_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='physicalserver',
            old_name='ExpireData',
            new_name='ExpireDate',
        ),
    ]
