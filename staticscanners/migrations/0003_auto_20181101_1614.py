# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staticscanners", "0002_auto_20181101_1454"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bandit_scan_db",
            name="total_dup",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bandit_scan_db",
            name="total_vuln",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="retirejs_scan_db",
            name="total_dup",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="retirejs_scan_db",
            name="total_vuln",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
