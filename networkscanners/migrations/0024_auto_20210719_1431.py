# Generated by Django 3.1.12 on 2021-07-19 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("networkscanners", "0023_auto_20210719_1431"),
        ("projects", "0014_auto_20210719_1431"),
    ]

    operations = [
        migrations.AddField(
            model_name="networkscandb",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.projectdb",
            ),
        ),
        migrations.AddField(
            model_name="networkscandb",
            name="updated_time",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="networkscanresultsdb",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.projectdb",
            ),
        ),
        migrations.AddField(
            model_name="networkscanresultsdb",
            name="updated_time",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="networkscandb",
            name="scanner",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name="networkscandb",
            table="networkscandb",
        ),
        migrations.AlterModelTable(
            name="networkscanresultsdb",
            table="networkscanresultsdb",
        ),
    ]
