from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Report(models.Model):
    mark = models.CharField(max_length=20, verbose_name='Марка машины')
    model = models.CharField(max_length=20, verbose_name='Модель машины')
    average_price = models.IntegerField(default=0, verbose_name='Средняя цена')
    #year_from = models.IntegerField(verbose_name="С какого года")
    #mileage = models.CharField(max_length=20, verbose_name='Пробег от: ')
    #price = models.CharField(max_length=20, verbose_name='Цена')
    #body_type = models.CharField(max_length=50, verbose_name='Модель кузова')
    #volume = models.CharField(max_length=50, verbose_name='Объем/КПП/Мощность')

    def __str__(self):
        return f'Марка: {self.mark}, Модель: {self.model}, Средняя цена: {self.average_price}'

    class Meta:
        verbose_name = 'список'
        verbose_name_plural = f'Отчет по ценам на аренду авто'


