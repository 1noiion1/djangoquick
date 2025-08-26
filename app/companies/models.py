from django.db import models
from django.conf import settings


class Company(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_company'
    )
    name = models.CharField(max_length=100, verbose_name='Название компании')
    inn = models.CharField(max_length=12, unique=True, verbose_name='ИНН компании')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания компании')


    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


    def __str__(self):
        return self.name
