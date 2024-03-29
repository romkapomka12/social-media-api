# Generated by Django 5.0.1 on 2024-01-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Discussion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField(blank=True, null=True)),
                ("is_read", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["timestamp"],
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="")),
                ("location", models.TextField(null=True)),
                ("description", models.TextField(max_length=144, null=True)),
                (
                    "hash_tags",
                    models.CharField(default=None, max_length=100, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
    ]
