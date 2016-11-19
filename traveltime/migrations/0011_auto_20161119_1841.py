# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traveltime', '0010_auto_20161119_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='LargeTown',
            fields=[
                ('place_name', models.CharField(max_length=180, primary_key=True, serialize=False)),
                ('admin_name1', models.CharField(max_length=100, null=True)),
                ('admin_name2', models.CharField(max_length=100, null=True)),
                ('admin_name3', models.CharField(max_length=100, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('pop', models.IntegerField()),
                ('route_ends', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place2', to='traveltime.DistanceMatrix')),
                ('route_starts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place1', to='traveltime.DistanceMatrix')),
            ],
        ),
        migrations.RemoveField(
            model_name='uk_location',
            name='route_ends',
        ),
        migrations.RemoveField(
            model_name='uk_location',
            name='route_starts',
        ),
    ]
