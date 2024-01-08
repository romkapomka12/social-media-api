# Generated by Django 5.0.1 on 2024-01-08 13:40

import user.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="userprofile",
            managers=[
                ("objects", user.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="userprofile",
            name="full_name",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
