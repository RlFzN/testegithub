# Generated by Django 2.1.8 on 2020-04-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staticscanners", "0016_nodejsscan_scan_db_nodejsscan_scan_results_db"),
    ]

    operations = [
        migrations.AddField(
            model_name="nodejsscan_scan_results_db",
            name="severity",
            field=models.TextField(blank=True, null=True),
        ),
    ]
