# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("networkscanners", "0006_scan_save_db_log_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="nessus_report_db",
            name="severity_color",
            field=models.TextField(blank=True, null=True),
        ),
    ]
