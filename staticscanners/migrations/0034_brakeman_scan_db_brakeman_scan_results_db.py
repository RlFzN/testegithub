# Generated by Django 3.1.5 on 2021-01-12 22:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staticscanners", "0033_twistlock_scan_db_twistlock_scan_results_db"),
    ]

    operations = [
        migrations.CreateModel(
            name="brakeman_scan_db",
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
                ("total_vul", models.IntegerField(blank=True, null=True)),
                ("scan_status", models.IntegerField(blank=True, null=True)),
                ("date_time", models.DateTimeField(blank=True, null=True)),
                ("total_dup", models.IntegerField(blank=True, null=True)),
                ("high_vul", models.IntegerField(blank=True, null=True)),
                ("medium_vul", models.IntegerField(blank=True, null=True)),
                ("low_vul", models.IntegerField(blank=True, null=True)),
                ("username", models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="brakeman_scan_results_db",
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
                ("date_time", models.DateTimeField(blank=True, null=True)),
                ("vuln_id", models.UUIDField(blank=True)),
                ("false_positive", models.TextField(blank=True, null=True)),
                ("vul_col", models.TextField(blank=True)),
                ("dup_hash", models.TextField(blank=True, null=True)),
                ("vuln_duplicate", models.TextField(blank=True, null=True)),
                ("false_positive_hash", models.TextField(blank=True, null=True)),
                ("vuln_status", models.TextField(blank=True, null=True)),
                ("severity", models.TextField(blank=True, null=True)),
                ("jira_ticket", models.TextField(blank=True, null=True)),
                ("scanner", models.TextField(default="brakeman", editable=False)),
                ("username", models.CharField(max_length=256, null=True)),
                ("name", models.TextField(blank=True, null=True)),
                ("warning_code", models.TextField(blank=True, null=True)),
                ("fingerprint", models.TextField(blank=True, null=True)),
                ("check_name", models.TextField(blank=True, null=True)),
                ("file", models.TextField(blank=True, null=True)),
                ("line", models.TextField(blank=True, null=True)),
                ("link", models.TextField(blank=True, null=True)),
                ("code", models.TextField(blank=True, null=True)),
                ("render_path", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
