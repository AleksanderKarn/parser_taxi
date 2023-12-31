# Generated by Django 4.2.2 on 2023-06-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=20, verbose_name='Марка машины')),
                ('model', models.CharField(max_length=20, verbose_name='Модель машины')),
                ('year_from', models.IntegerField(verbose_name='С какого года')),
                ('mileage', models.IntegerField(verbose_name='Пробег от: ')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'список',
                'verbose_name_plural': 'Список ТС на Auto.ru',
            },
        ),
    ]
