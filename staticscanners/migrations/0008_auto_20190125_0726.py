# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-25 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staticscanners", "0007_findbugs_scan_results_db_risk"),
    ]

    operations = [
        migrations.AddField(
            model_name="bandit_scan_results_db",
            name="scanner",
            field=models.TextField(default="Bandit", editable=False, max_length=15),
        ),
        migrations.AddField(
            model_name="dependencycheck_scan_results_db",
            name="scanner",
            field=models.TextField(default="Dependency Check", editable=False),
        ),
        migrations.AddField(
            model_name="findbugs_scan_results_db",
            name="scanner",
            field=models.TextField(default="Findbugs", editable=False),
        ),
        migrations.AddField(
            model_name="retirejs_scan_results_db",
            name="scanner",
            field=models.TextField(default="RetireJs", editable=False),
        ),
    ]
