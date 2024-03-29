# Generated by Django 3.1.2 on 2020-10-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0011_auto_20200609_0735"),
    ]

    operations = [
        migrations.AlterField(
            model_name="month_db",
            name="high",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="month_db",
            name="low",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="month_db",
            name="medium",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="high_net",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="high_static",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="high_web",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="low_net",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="low_static",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="low_web",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="medium_net",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="medium_static",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="medium_web",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_close",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_false",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_high",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_low",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_medium",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_net",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_open",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_static",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_vuln",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project_db",
            name="total_web",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
