# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-26 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staticscanners", "0012_auto_20190824_0202"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bandit_scan_results_db",
            name="more_info",
            field=models.TextField(blank=True, null=True),
        ),
    ]
