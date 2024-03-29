# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-09 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webscanners", "0013_burp_scan_result_db_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="reference",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="remediation",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="vulnerability_classifications",
            field=models.TextField(blank=True, null=True),
        ),
    ]
