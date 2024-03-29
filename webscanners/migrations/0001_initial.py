# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-04 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="zap_scan_results_db",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vuln_id", models.TextField(blank=True)),
                ("scan_id", models.TextField(blank=True)),
                ("confidence", models.TextField(blank=True)),
                ("wascid", models.TextField(blank=True)),
                ("cweid", models.TextField(blank=True)),
                ("risk", models.TextField(blank=True)),
                ("reference", models.TextField(blank=True)),
                ("url", models.TextField(blank=True)),
                ("name", models.TextField(blank=True)),
                ("solution", models.TextField(blank=True)),
                ("param", models.TextField(blank=True)),
                ("evidence", models.TextField(blank=True)),
                ("sourceid", models.TextField(blank=True)),
                ("pluginId", models.TextField(blank=True)),
                ("other", models.TextField(blank=True)),
                ("attack", models.TextField(blank=True)),
                ("messageId", models.TextField(blank=True)),
                ("method", models.TextField(blank=True)),
                ("alert", models.TextField(blank=True)),
                ("ids", models.TextField(blank=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="zap_scans_db",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("scan_url", models.TextField(blank=True)),
                ("scan_scanid", models.TextField(blank=True)),
                ("vul_num", models.TextField(blank=True)),
                ("vul_status", models.TextField(blank=True)),
                ("total_vul", models.TextField(blank=True)),
                ("high_vul", models.TextField(blank=True)),
                ("medium_vul", models.TextField(blank=True)),
                ("low_vul", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="zap_spider_db",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("spider_url", models.TextField(blank=True)),
                ("spider_scanid", models.TextField(blank=True)),
                ("urls_num", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="zap_spider_results",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("spider_id", models.TextField(blank=True)),
                ("spider_urls", models.TextField(blank=True)),
            ],
        ),
    ]
