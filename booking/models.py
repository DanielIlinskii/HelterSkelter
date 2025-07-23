from urllib import request
from django.db import models
from CRM import settings
from users.models import User
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Status(models.TextChoices):
    later = "Later", "Предстоит"
    done = "Done", "Выполнено"
    canceled = "Canceled", "Отменено"

# Валидатор для телефона
phone_validator = RegexValidator(
    regex=r"^\+?7?\d{9,15}$",
    message="Номер телефона должен быть в формате: '+79991234567'. Допускается до 15 цифр.",
)


class Booking(models.Model):
    TARIFF_CHOICES = [
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
    ]

    WORK_TYPE_CHOICES = [
        ("a", "Тип A"),
        ("b", "Тип B"),
        ("c", "Тип C"),
        ("d", "Тип D"),
        ("e", "Тип E"),
        ("f", "Тип F"),
        ("g", "Тип G"),
    ]

    client_name = models.CharField("Имя клиента", max_length=100)
    client_phone = models.CharField(
        "Телефон клиента", max_length=20, validators=[phone_validator]
    )
    booking_datetime = models.DateTimeField("Дата и время записи")
    tariff = models.CharField("Тариф", max_length=1, choices=TARIFF_CHOICES)
    work_type = models.CharField("Тип работы", max_length=1, choices=WORK_TYPE_CHOICES)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        unique_together = ("client_phone", "booking_datetime")
        indexes = [
            models.Index(fields=["booking_datetime"]),
        ]

    def __str__(self):
        return f"{self.client_name} — {self.booking_datetime.strftime('%d.%m %H:%M')}"
