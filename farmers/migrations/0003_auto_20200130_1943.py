# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-30 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0002_auto_20200130_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='time_type',
            field=models.CharField(choices=[('m_1', '1 Month'), ('m_3', '3 Months'), ('m_6', '6 Month'), ('m_12', '12 Month')], max_length=3),
        ),
    ]
