# Generated by Django 3.1.8 on 2021-05-31 20:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("networkscanners", "0018_networkscandb_networkscanresultsdb"),
    ]

    operations = [
        migrations.DeleteModel(
            name="nessus_report_db",
        ),
        migrations.DeleteModel(
            name="nessus_scan_db",
        ),
        migrations.DeleteModel(
            name="nessus_scan_results_db",
        ),
        migrations.DeleteModel(
            name="nessus_targets_db",
        ),
        migrations.AddField(
            model_name="networkscanresultsdb",
            name="vuln_status",
            field=models.TextField(blank=True, null=True),
        ),
    ]
