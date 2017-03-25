# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_installation_room_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='room_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='installation',
            name='room_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
