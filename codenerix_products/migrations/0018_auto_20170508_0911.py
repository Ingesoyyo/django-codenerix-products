# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 09:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0017_auto_20170505_1146'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OptionValues',
        ),
        migrations.AlterModelOptions(
            name='optionvalueattribute',
            options={},
        ),
        migrations.AlterModelOptions(
            name='optionvaluefeature',
            options={},
        ),
        migrations.AlterModelOptions(
            name='optionvaluefeaturespecial',
            options={},
        ),
    ]
