from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from mainapp.models import NULLABLE


class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name=_("Email"), unique=True)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", **NULLABLE)
    avatar = models.ImageField(upload_to="users", **NULLABLE)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
