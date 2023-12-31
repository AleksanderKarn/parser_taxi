from django.db import models

NULLABLE = {'blank': True, 'null': True}


class ArendaCar(models.Model):
    cars = models.CharField(max_length=500, verbose_name='Маркаи машин', default='')
    price = models.CharField(max_length=20, verbose_name='Цена из объявления')
    #link = models.CharField(max_length=200, verbose_name='Ссылка', default='')
    taxopark = models.CharField(max_length=200, verbose_name='название компании', default='')
    description = models.TextField(verbose_name='Описание объявления', default='')
    schedule = models.CharField(max_length=20, verbose_name='Граффик', default='не указан')
    #placement_date = models.CharField(max_length=30, verbose_name='дата размещения', default='')
    #komission_park = models.CharField(max_length=30, verbose_name='Комиссия парка', default='-')
    #usloviya_vivoda_sredstv = models.CharField(max_length=200, verbose_name="Условия вывода", default='-')

    def __str__(self):
        return f'{self.cars} '

    class Meta:
        verbose_name = 'Список аренды авто Avito'
        verbose_name_plural = 'Список аренды авто Avito'
