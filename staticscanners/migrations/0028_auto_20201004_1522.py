# Generated by Django 3.1.2 on 2020-10-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "staticscanners",
            "0027_gitlabcontainerscan_scan_db_gitlabcontainerscan_scan_results_db",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="bandit_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="checkmarx_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="clair_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="dependencycheck_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="findbugs_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="gitlabcontainerscan_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="gitlabsast_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="gitlabsca_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="nodejsscan_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="npmaudit_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="retirejs_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="semgrepscan_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="tfsec_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="trivy_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="whitesource_scan_results_db",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
