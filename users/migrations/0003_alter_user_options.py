# Generated by Django 4.2.21 on 2025-05-14 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_access_level_alter_user_activity_history_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
