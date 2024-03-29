# Generated by Django 3.1.12 on 2021-07-19 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0014_auto_20210719_1431"),
        ("staticscanners", "0035_auto_20210601_1830"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="staticscanresultsdb",
            options={"verbose_name_plural": "Static Scans Data"},
        ),
        migrations.AlterModelOptions(
            name="staticscansdb",
            options={"verbose_name_plural": "Static Scans Db"},
        ),
        migrations.RemoveField(
            model_name="staticscanresultsdb",
            name="project_id",
        ),
        migrations.RemoveField(
            model_name="staticscanresultsdb",
            name="username",
        ),
        migrations.RemoveField(
            model_name="staticscansdb",
            name="project_id",
        ),
        migrations.RemoveField(
            model_name="staticscansdb",
            name="username",
        ),
        migrations.AddField(
            model_name="staticscanresultsdb",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.projectdb",
            ),
        ),
        migrations.AddField(
            model_name="staticscanresultsdb",
            name="updated_time",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="staticscansdb",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.projectdb",
            ),
        ),
        migrations.AddField(
            model_name="staticscansdb",
            name="updated_time",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="staticscanresultsdb",
            name="scanner",
            field=models.TextField(blank=True),
        ),
        migrations.AlterModelTable(
            name="staticscanresultsdb",
            table="staticscanresultsdb",
        ),
        migrations.AlterModelTable(
            name="staticscansdb",
            table="staticscansdb",
        ),
    ]
