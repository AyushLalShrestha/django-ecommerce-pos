# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_available', models.BooleanField(default=True, verbose_name='Availability ?')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Product')),
            ],
        ),
    ]