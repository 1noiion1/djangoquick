from django.db import models
from django.conf import settings


class Storage(models.Model):
    company = models.OneToOneField(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='storage'
    )
    address = models.CharField(max_length=250, verbose_name='Адрес склада')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')


    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


    def __str__(self):
        return f'Склад компании - {self.company.name}'
