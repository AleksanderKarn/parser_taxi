from django.db import models

NULLABLE = {'blank': True, 'null': True}


class CarListAvito(models.Model):
    mark = models.CharField(max_length=20, verbose_name='Марка машины')
    model = models.CharField(max_length=20, verbose_name='Модель машины')
    year_from = models.IntegerField(verbose_name="С какого года")
    mileage = models.CharField(max_length=20, verbose_name='Пробег от: ')
    price = models.CharField(max_length=20, verbose_name='Цена')
    body_type = models.CharField(max_length=50, verbose_name='Модель кузова')
    volume = models.CharField(max_length=50, verbose_name='Объем/КПП/Мощность')

    def __str__(self):
        return f'Марка: {self.mark}, Модель: {self.model}, Год: {self.year_from}, Пробег: {self.mileage}, Цена: {self.price}'

    class Meta:
        verbose_name = 'список'
        verbose_name_plural = f'Список ТС на AVITO'


