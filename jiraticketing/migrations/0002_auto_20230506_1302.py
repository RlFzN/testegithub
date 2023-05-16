# Generated by Django 3.2.15 on 2023-05-06 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_management", "0001_initial"),
        ("jiraticketing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jirasetting",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jira_ticket_db_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="jirasetting",
            name="created_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="jirasetting",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="jirasetting",
            name="organization",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_management.organization",
            ),
        ),
        migrations.AddField(
            model_name="jirasetting",
            name="updated_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jira_ticket_db_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
