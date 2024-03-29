# Generated by Django 3.2.15 on 2023-05-06 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_management", "0001_initial"),
        ("staticscanners", "0037_staticscanresultsdb_note"),
    ]

    operations = [
        migrations.AddField(
            model_name="staticscanresultsdb",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="static_scan_result_db_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="staticscanresultsdb",
            name="created_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="staticscanresultsdb",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="staticscanresultsdb",
            name="organization",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_management.organization",
            ),
        ),
        migrations.AddField(
            model_name="staticscanresultsdb",
            name="updated_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="static_scan_result_db_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="staticscansdb",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="static_scan_db_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="staticscansdb",
            name="created_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="staticscansdb",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="staticscansdb",
            name="organization",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_management.organization",
            ),
        ),
        migrations.AddField(
            model_name="staticscansdb",
            name="updated_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="static_scan_db_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
