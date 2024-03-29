# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-08 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webscanners", "0010_burp_issue_definitions_remediation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="host",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="issueBackground",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="issueDetail",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="location",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="method",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="path",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="references",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="remediationBackground",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="requestresponse",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="scan_request",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="scan_response",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="serialNumber",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="severity_color",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="types",
        ),
        migrations.RemoveField(
            model_name="burp_scan_result_db",
            name="vulnerabilityClassifications",
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="caption",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="internal_data",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="origin",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="request_response_request_data",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="request_response_request_type",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="request_response_response_data",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="request_response_response_type",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="request_response_url",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="request_time",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="serial_number",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="type_index",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="burp_scan_result_db",
            name="was_redirect_followed",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="burp_scan_result_db",
            name="confidence",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="burp_scan_result_db",
            name="name",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="burp_scan_result_db",
            name="severity",
            field=models.TextField(blank=True, null=True),
        ),
    ]
