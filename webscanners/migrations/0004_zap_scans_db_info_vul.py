# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-26 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webscanners", "0003_auto_20190207_0331"),
    ]

    operations = [
        migrations.AddField(
            model_name="zap_scans_db",
            name="info_vul",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
