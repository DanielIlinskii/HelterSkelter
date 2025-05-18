from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import (
    PhoneNumberField,
)  # Для валидации номера телефона


class AccessLevel(models.TextChoices):
    CLIENT = "client", "Клиент"
    ADMIN = "admin", "Админ"
    OWNER = "owner", "Владелец"


class User(AbstractUser):
    # Поле username оставляем, но делаем email уникальным
    name = models.CharField("Имя", blank=True)
    last_name = models.CharField("Фамилия", blank=True)
    username = models.CharField("Логин", blank=True, unique=True)
    email = models.EmailField("Почта", unique=True)
    phone_number = models.CharField("Номер телефона", blank=True, unique=True)
    balance = models.DecimalField(
        "Баланс", max_digits=10, decimal_places=2, default=0.0
    )
    last_login = models.DateTimeField("Был в сети", blank=True, null=True)
    is_verified = models.BooleanField("Пройдена верификация", default=False)
    access_level = models.CharField(
        "Уровень доступа",
        max_length=10,
        choices=AccessLevel.choices,
        default=AccessLevel.CLIENT,
    )

    # Дополнительные поля
    date_of_birth = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField("Пол", max_length=10, blank=True)
    address = models.CharField("Адресс", max_length=255, blank=True)
    registration_date = models.DateTimeField("Дата регистрации", auto_now_add=True)
    visits_count = models.PositiveIntegerField("Кол-во посещений", default=0)
    activity_history = models.JSONField("История активности", default=list, blank=True)
    is_subscribed = models.BooleanField("Подписан", default=True)
    preferred_contact_method = models.CharField(
        "Предпочтительный способ связи", max_length=20, blank=True
    )
    transaction_history = models.JSONField(
        "История транзакций", default=list, blank=True
    )
    loyalty_discount = models.DecimalField(
        "Скидка", max_digits=5, decimal_places=2, default=0.0
    )
    allergies = models.TextField("Аллергии", blank=True)
    special_notes = models.TextField("Заметки", blank=True)
    social_media_links = models.JSONField("Соц. сети", default=dict, blank=True)
    referral_code = models.CharField(
        "Реферальный код", max_length=50, unique=True, null=True, blank=True
    )
    source_of_signup = models.CharField("Откуда узнал о нас", max_length=50, blank=True)

    # Настройки
    USERNAME_FIELD = "username"  # Используем phone_number как основной идентификатор
    # REQUIRED_FIELDS = [
    #     "username"
    # ]  # username теперь обязателен при создании пользователя

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name + " " + self.last_name
