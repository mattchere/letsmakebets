# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0003_auto_20171113_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='accepted',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
