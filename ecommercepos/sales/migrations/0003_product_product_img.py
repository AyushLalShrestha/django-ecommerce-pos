# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.FileField(default='anony.jpg', upload_to=''),
        ),
    ]
