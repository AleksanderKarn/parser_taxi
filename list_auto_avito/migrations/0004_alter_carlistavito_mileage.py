# Generated by Django 4.2.2 on 2023-06-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_auto_avito', '0003_alter_carlistavito_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlistavito',
            name='mileage',
            field=models.CharField(default=1000, max_length=20, verbose_name='Пробег от: '),
        ),
    ]
