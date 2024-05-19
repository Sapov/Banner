from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    """Роли пользователей"""

    CUSTOMER_RETAIL = "CUSTOMER_RETAIL", "Клиент"  # розничный клиент
    CUSTOMER_AGENCY = "CUSTOMER_AGENCY", "Рекламное агентство"  # Рекламное агентство
    MANAGER = "MANAGER", "Менеджер"
    OPERATOR = "OPERATOR", "Оператор"
    FINANCIER = "FINANCIER", "Бухгалтер"


class Users(AbstractUser):
    role = models.CharField(
        max_length=24, choices=Role.choices, default=Role.CUSTOMER_RETAIL
    )
    phone = models.CharField(max_length=16, verbose_name="Телефон")
