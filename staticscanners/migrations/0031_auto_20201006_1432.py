# Generated by Django 3.1.2 on 2020-10-06 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staticscanners', '0030_auto_20201006_0858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bandit_scan_db',
            old_name='SEVERITY_HIGH',
            new_name='high_vul',
        ),
    ]
