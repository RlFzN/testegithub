# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("networkscanners", "0002_auto_20181031_0022"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nessus_scan_db",
            name="critical_total",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="nessus_scan_db",
            name="high_total",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="nessus_scan_db",
            name="low_total",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="nessus_scan_db",
            name="medium_total",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="nessus_scan_db",
            name="total_dup",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="nessus_scan_db",
            name="total_vul",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="scan_save_db",
            name="high_total",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="scan_save_db",
            name="low_total",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="scan_save_db",
            name="medium_total",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="scan_save_db",
            name="total_dup",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="scan_save_db",
            name="total_vul",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
