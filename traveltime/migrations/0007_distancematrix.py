# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traveltime', '0006_auto_20161119_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistanceMatrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linear_distance', models.IntegerField()),
                ('place1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='p1', to='traveltime.uk_location')),
                ('place2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='p2', to='traveltime.uk_location')),
            ],
        ),
    ]