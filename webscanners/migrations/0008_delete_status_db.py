# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-11 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("webscanners", "0007_status_db"),
    ]

    operations = [
        migrations.DeleteModel(
            name="status_db",
        ),
    ]
