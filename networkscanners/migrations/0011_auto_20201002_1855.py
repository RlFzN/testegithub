# Generated by Django 3.1.1 on 2020-10-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("networkscanners", "0010_auto_20201002_1836"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nessus_scan_results_db",
            name="vul_id",
            field=models.TextField(blank=True, null=True),
        ),
    ]
