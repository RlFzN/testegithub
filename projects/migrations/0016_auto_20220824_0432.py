# Generated by Django 3.2.15 on 2022-08-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0015_auto_20210719_1431"),
    ]

    operations = [
        migrations.AddField(
            model_name="monthdb",
            name="critical",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name="projectdb",
            name="critical_net",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="projectdb",
            name="critical_static",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="projectdb",
            name="critical_web",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="projectdb",
            name="total_critical",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
