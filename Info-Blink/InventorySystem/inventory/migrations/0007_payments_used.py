# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20170706_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
