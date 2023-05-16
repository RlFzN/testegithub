# Generated by Django 3.2.15 on 2023-05-06 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_management", "0001_initial"),
        ("projects", "0018_auto_20220826_1608"),
    ]

    operations = [
        migrations.AddField(
            model_name="monthdb",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="month_creator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="monthdb",
            name="created_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="monthdb",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="monthdb",
            name="organization",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_management.organization",
            ),
        ),
        migrations.AddField(
            model_name="monthdb",
            name="updated_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="month_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="projectdb",
            name="organization",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_management.organization",
            ),
        ),
        migrations.AddField(
            model_name="projectscandb",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="project_scan_creator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="projectscandb",
            name="created_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="projectscandb",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="projectscandb",
            name="organization",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_management.organization",
            ),
        ),
        migrations.AddField(
            model_name="projectscandb",
            name="updated_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="project_scan_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="projectdb",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="project_db_creator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="projectdb",
            name="created_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="projectdb",
            name="updated_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="project_db_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
