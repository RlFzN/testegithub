# Generated by Django 3.1.12 on 2021-08-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("archeryapi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orgapikey",
            name="name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
