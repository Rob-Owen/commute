# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltime', '0002_auto_20161119_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='population',
            name='region_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
