# Generated by Django 5.0.1 on 2024-01-12 09:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_alter_userprofile_managers_userprofile_full_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userprofile",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
    ]
