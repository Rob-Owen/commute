# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltime', '0008_auto_20161119_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='population',
            name='id',
        ),
        migrations.AlterField(
            model_name='population',
            name='place_name',
            field=models.CharField(max_length=180, primary_key=True, serialize=False),
        ),
    ]
