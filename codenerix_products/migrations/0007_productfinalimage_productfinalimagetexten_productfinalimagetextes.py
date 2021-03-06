# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 10:22
from __future__ import unicode_literals

import codenerix.fields
import codenerix.lib.helpers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0006_auto_20170331_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFinalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('image', codenerix.fields.ImageAngularField(max_length=200, upload_to=codenerix.lib.helpers.upload_path, verbose_name='Image')),
                ('order', models.SmallIntegerField(blank=True, null=True, verbose_name='Order')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('principal', models.BooleanField(default=False, verbose_name='Principal')),
                ('flagship_product', models.BooleanField(default=False, verbose_name='Flagship product')),
                ('outstanding', models.BooleanField(default=False, verbose_name='Outstanding')),
                ('product_final', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productfinals_image', to='codenerix_products.ProductFinal', verbose_name='Product Final')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductFinalImageTextEN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('product_final_image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='en', to='codenerix_products.ProductFinalImage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductFinalImageTextES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('product_final_image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='es', to='codenerix_products.ProductFinalImage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
