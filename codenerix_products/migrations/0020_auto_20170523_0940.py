# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0019_productfinal_ean13'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='recargo_equivalencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='codenerix_products.TypeRecargoEquivalencia', verbose_name='Recargo Equivalencia (%)'),
        ),
    ]