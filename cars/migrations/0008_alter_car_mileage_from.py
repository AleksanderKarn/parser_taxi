# Generated by Django 4.2.2 on 2023-06-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_mileage_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage_from',
            field=models.IntegerField(default=1000, verbose_name='Пробег от: '),
        ),
    ]
