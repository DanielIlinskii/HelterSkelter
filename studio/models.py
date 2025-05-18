from django.db import models


class Studio(models.Model):
    address = models.CharField("Адрес", max_length=255)
    phone_number = models.CharField("Номер телефона студии", max_length=255)
    description = models.TextField(
        "Описании студии",
    )
    who_admin = models.ForeignKey(
        "users.User",
        verbose_name="Администратор",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = "Студия"
        verbose_name_plural = "Студии"

    def __str__(self):
        return self.address
