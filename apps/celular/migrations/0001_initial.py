# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='celular',
            fields=[
                ('id_celular', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('fabricante', models.CharField(max_length=30)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.FloatField()),
            ],
        ),
    ]