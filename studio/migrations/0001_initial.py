# Generated by Django 4.2.21 on 2025-05-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Studio",
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
                ("address", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("who_admin", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Студия",
                "verbose_name_plural": "Студии",
            },
        ),
    ]
