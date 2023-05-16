# Generated by Django 2.1.8 on 2020-08-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staticscanners", "0022_auto_20200823_1753"),
    ]

    operations = [
        migrations.CreateModel(
            name="checkmarx_scan_db",
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
                ("scan_id", models.UUIDField(blank=True, null=True)),
                ("rescan_id", models.TextField(blank=True, null=True)),
                ("scan_date", models.TextField(blank=True, null=True)),
                ("project_id", models.UUIDField(blank=True, null=True)),
                ("project_name", models.TextField(blank=True, null=True)),
                ("total_vuln", models.IntegerField(blank=True, null=True)),
                ("scan_status", models.IntegerField(blank=True, null=True)),
                ("date_time", models.DateTimeField(blank=True, null=True)),
                ("total_dup", models.IntegerField(blank=True, null=True)),
                ("SEVERITY_HIGH", models.IntegerField(blank=True, null=True)),
                ("SEVERITY_MEDIUM", models.IntegerField(blank=True, null=True)),
                ("SEVERITY_LOW", models.IntegerField(blank=True, null=True)),
                ("username", models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="checkmarx_scan_results_db",
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
                ("scan_id", models.UUIDField(blank=True)),
                ("rescan_id", models.TextField(blank=True, null=True)),
                ("scan_date", models.TextField(blank=True)),
                ("project_id", models.UUIDField(blank=True)),
                ("vuln_id", models.UUIDField(blank=True)),
                ("false_positive", models.TextField(blank=True, null=True)),
                ("vul_col", models.TextField(blank=True)),
                ("dup_hash", models.TextField(blank=True, null=True)),
                ("vuln_duplicate", models.TextField(blank=True, null=True)),
                ("false_positive_hash", models.TextField(blank=True, null=True)),
                ("vuln_status", models.TextField(blank=True, null=True)),
                ("name", models.TextField(blank=True)),
                ("scan_details", models.TextField(blank=True)),
                ("query", models.TextField(blank=True)),
                ("severity", models.TextField(blank=True)),
                ("result", models.TextField(blank=True)),
                ("scanner", models.TextField(default="Checkmarx", editable=False)),
                ("jira_ticket", models.TextField(blank=True, null=True)),
                ("username", models.CharField(max_length=256, null=True)),
            ],
        ),
    ]
