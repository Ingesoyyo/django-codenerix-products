# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 08:50
from __future__ import unicode_literals

import codenerix.multiforms
import codenerix.views
import codenerix_products.views
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0009_brand_show_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImageCreate',
            fields=[
                ('productimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='codenerix_products.ProductImage')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
            bases=(codenerix_products.views.GenProductImageUrl, 'codenerix_products.productimage', codenerix.multiforms.MultiForm, codenerix.views.GenCreate),
        ),
        migrations.CreateModel(
            name='ProductImageUpdate',
            fields=[
                ('productimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='codenerix_products.ProductImage')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
            bases=(codenerix_products.views.GenProductImageUrl, 'codenerix_products.productimage', codenerix.multiforms.MultiForm, codenerix.views.GenUpdate),
        ),
        migrations.AddField(
            model_name='attribute',
            name='name_file',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='brand',
            name='name_file',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='family',
            name='name_file',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='feature',
            name='name_file',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='featurespecial',
            name='name_file',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='flagshipproduct',
            name='name_file',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productfinalimage',
            name='name_file',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='name_file',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Name'),
        ),
        migrations.CreateModel(
            name='ProductImageCreateModal',
            fields=[
                ('productimagecreate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='codenerix_products.ProductImageCreate')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
            bases=(codenerix.views.GenCreateModal, 'codenerix_products.productimagecreate'),
        ),
        migrations.CreateModel(
            name='ProductImageUpdateModal',
            fields=[
                ('productimageupdate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='codenerix_products.ProductImageUpdate')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
            bases=(codenerix.views.GenUpdateModal, 'codenerix_products.productimageupdate'),
        ),
    ]
