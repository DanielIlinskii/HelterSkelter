# Generated by Django 5.2.3 on 2025-07-23 13:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                (
                    "client_name",
                    models.CharField(max_length=100, verbose_name="Имя клиента"),
                ),
                (
                    "client_phone",
                    models.CharField(
                        max_length=20,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Номер телефона должен быть в формате: '+79991234567'. Допускается до 15 цифр.",
                                regex="^\\+?7?\\d{9,15}$",
                            )
                        ],
                        verbose_name="Телефон клиента",
                    ),
                ),
                (
                    "booking_datetime",
                    models.DateTimeField(verbose_name="Дата и время записи"),
                ),
                (
                    "tariff",
                    models.CharField(
                        choices=[("S", "S"), ("M", "M"), ("L", "L")],
                        max_length=1,
                        verbose_name="Тариф",
                    ),
                ),
                (
                    "work_type",
                    models.CharField(
                        choices=[
                            ("a", "Тип A"),
                            ("b", "Тип B"),
                            ("c", "Тип C"),
                            ("d", "Тип D"),
                            ("e", "Тип E"),
                            ("f", "Тип F"),
                            ("g", "Тип G"),
                        ],
                        max_length=1,
                        verbose_name="Тип работы",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
                "indexes": [
                    models.Index(
                        fields=["booking_datetime"],
                        name="booking_boo_booking_558d21_idx",
                    )
                ],
                "unique_together": {("client_phone", "booking_datetime")},
            },
        ),
        migrations.DeleteModel(
            name="Schedule",
        ),
    ]
