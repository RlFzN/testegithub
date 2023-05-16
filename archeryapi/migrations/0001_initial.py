# Generated by Django 3.1.12 on 2021-08-04 18:38

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OrgAPIKey",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uu_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("api_key", models.CharField(max_length=255)),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="key_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Organization API Keys",
                "db_table": "org_apikey",
            },
        ),
    ]
