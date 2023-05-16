# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-07 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staticscanners", "0008_auto_20190125_0726"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bandit_scan_db",
            name="CONFIDENCE_HIGH",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bandit_scan_db",
            name="CONFIDENCE_LOW",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bandit_scan_db",
            name="SEVERITY_HIGH",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bandit_scan_db",
            name="SEVERITY_LOW",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bandit_scan_db",
            name="SEVERITY_MEDIUM",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bandit_scan_results_db",
            name="scanner",
            field=models.TextField(default="Bandit", editable=False),
        ),
        migrations.AlterField(
            model_name="dependencycheck_scan_db",
            name="SEVERITY_HIGH",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dependencycheck_scan_db",
            name="SEVERITY_LOW",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dependencycheck_scan_db",
            name="SEVERITY_MEDIUM",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dependencycheck_scan_results_db",
            name="scanner",
            field=models.TextField(default="Dependency Check", editable=False),
        ),
        migrations.AlterField(
            model_name="findbugs_scan_db",
            name="SEVERITY_HIGH",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="findbugs_scan_db",
            name="SEVERITY_LOW",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="findbugs_scan_db",
            name="SEVERITY_MEDIUM",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="findbugs_scan_results_db",
            name="scanner",
            field=models.TextField(default="Findbugs", editable=False),
        ),
        migrations.AlterField(
            model_name="retirejs_scan_db",
            name="SEVERITY_HIGH",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="retirejs_scan_db",
            name="SEVERITY_LOW",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="retirejs_scan_db",
            name="SEVERITY_MEDIUM",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="retirejs_scan_results_db",
            name="scanner",
            field=models.TextField(default="RetireJs", editable=False),
        ),
    ]
