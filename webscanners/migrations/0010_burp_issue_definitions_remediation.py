# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webscanners", "0009_burp_issue_definitions"),
    ]

    operations = [
        migrations.AddField(
            model_name="burp_issue_definitions",
            name="remediation",
            field=models.TextField(blank=True, null=True),
        ),
    ]
