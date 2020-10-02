# Generated by Django 2.1.8 on 2020-05-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticscanners', '0018_tfsec_scan_db_tfsec_scan_results_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandit_scan_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='bandit_scan_results_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='clair_scan_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='clair_scan_results_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='dependencycheck_scan_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='dependencycheck_scan_results_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='findbugs_scan_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='findbugs_scan_results_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='nodejsscan_scan_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='nodejsscan_scan_results_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='npmaudit_scan_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='npmaudit_scan_results_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='retirejs_scan_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='retirejs_scan_results_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='tfsec_scan_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='tfsec_scan_results_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trivy_scan_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trivy_scan_results_db',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
