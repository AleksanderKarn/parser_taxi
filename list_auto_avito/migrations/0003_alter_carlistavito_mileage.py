# Generated by Django 4.2.2 on 2023-06-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_auto_avito', '0002_alter_carlistavito_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlistavito',
            name='mileage',
            field=models.CharField(max_length=20, verbose_name='Пробег от: '),
        ),
    ]
