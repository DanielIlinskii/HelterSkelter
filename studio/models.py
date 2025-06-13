from turtle import up
from django.db import models
from sqlalchemy import Null


class Studio(models.Model):
    address = models.CharField("Адрес", max_length=255)
    phone_number = models.CharField(
        "Номер телефона админа", max_length=255, blank=True, null=True
    )
    description = models.TextField(
        "Описании студии",
    )
    who_admin = models.OneToOneField(
        "users.User",
        verbose_name="Администратор",
        on_delete=models.SET_NULL,
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.who_admin:
            self.phone_number = self.who_admin.phone_number
            self.who_admin.where_admin = self.address
        else:
            self.phone_number = Null
        super().save(*args, **kwargs)

        self.who_admin.save(update_fields=["where_admin"])

    class Meta:
        verbose_name = "Студия"
        verbose_name_plural = "Студии"

    def __str__(self):
        return self.address
