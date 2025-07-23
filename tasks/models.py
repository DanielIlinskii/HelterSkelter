import re
from django.db import models
from CRM import settings


# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    performer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    do_by = models.DateTimeField()
    title = models.TextField()
    status = models.ChoicesField(
        choices=(
            ("high", "Высокий"),
            ("middle", "Средний"),
            ("low", "Низкий"),
        ),
        default="low",
    )

    def save(self, *args, **kwargs):
        user = hasattr(self, "_user")
        if user.access_level not in ('admin', 'owner'):
            self.performer = self.author

        super().save(*args, **kwargs)
