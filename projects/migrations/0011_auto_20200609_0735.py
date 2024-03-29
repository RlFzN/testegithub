# Generated by Django 3.1.2 on 2020-06-09 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0010_month_db_project_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="month_db",
            name="high",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="month_db",
            name="low",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="month_db",
            name="medium",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="month_db",
            name="month",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="month_db",
            name="project_id",
            field=models.TextField(blank=True, null=True),
        ),
    ]
