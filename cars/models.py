from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Car(models.Model):

    mark = models.CharField(max_length=20, verbose_name='Марка машины')
    model = models.CharField(max_length=20, verbose_name='Модель машины')
    year_from = models.IntegerField(verbose_name="С какого года", default=2020)
    mileage_from = models.IntegerField(verbose_name='Пробег от: ', default=10000)
    mileage_to = models.IntegerField(verbose_name='Пробег до:', default=1000000)

    def __str__(self):
        return f'{self.mark}{self.model}{self.year_from}{self.mileage_from}#{self.mileage_to}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Поиск подробных ТС на Auto.ru'
