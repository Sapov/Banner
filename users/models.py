from django.contrib.auth.models import AbstractUser
from django.db import models

from mysite import settings


class Role(models.TextChoices):
    """Роли пользователей"""

    CUSTOMER_RETAIL = "CUSTOMER_RETAIL", "Клиент"  # розничный клиент
    CUSTOMER_AGENCY = "CUSTOMER_AGENCY", "Рекламное агентство"  # Рекламное агентство
    MANAGER = "MANAGER", "Менеджер"
    OPERATOR = "OPERATOR", "Оператор"
    FINANCIER = "FINANCIER", "Бухгалтер"


class CustomUsers(AbstractUser):
    role = models.CharField(
        max_length=24, choices=Role.choices, default=Role.CUSTOMER_RETAIL
    )
    phone = models.CharField(max_length=16, verbose_name="Телефон")
    organisation = models.ForeignKey(
        "Organisation", on_delete=models.CASCADE, null=True
    )


class Organisation(models.Model):
    Contractor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="ЗАКАЗЧИК!!",
        default=1,
    )
    name_ul = models.CharField(
        max_length=70,
        verbose_name="Имя юр. лица",
        help_text="Форма собственности и название.Если платильщик физ. Лицо, оаставить физ. лицо. ",
        default='Физ. лицо'
    )
    address_ur = models.TextField(
        null=True,
        blank=True,
        verbose_name="Юр. Адрес",
        help_text="Полный почтовый адрес",
    )
    address_post = models.TextField(
        null=True, blank=True, verbose_name="Почтовый Адрес"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    phone2 = models.CharField(
        max_length=20, blank=True, verbose_name="Телефон резервный"
    )
    email = models.EmailField(
        max_length=20, blank=True, verbose_name="Электронная почта"
    )
    inn = models.CharField(max_length=12, verbose_name="ИНН", blank=True)
    kpp = models.CharField(max_length=9, verbose_name="КПП", blank=True)
    okpo = models.CharField(max_length=12, blank=True, verbose_name="ОКПО")
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Опубликовано"
    )

    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Организации"
        verbose_name = "Организация"
        ordering = ["name_ul"]

    def __str__(self):
        return self.name_ul
