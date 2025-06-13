from urllib import request
from django.db import models
from CRM import settings
from users.models import User

# Create your models here.


class Status(models.TextChoices):
    later = "Later", "Предстоит"
    done = "Done", "Выполнено"
    canceled = "Canceled", "Отменено"


class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    type_of_work = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255, choices=Status.choices, default=Status.later
    )

    master = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )