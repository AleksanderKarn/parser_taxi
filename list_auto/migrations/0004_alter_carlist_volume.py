# Generated by Django 4.2.2 on 2023-06-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_auto', '0003_remove_carlist_power_remove_carlist_transmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlist',
            name='volume',
            field=models.CharField(max_length=50, verbose_name='Объем/КПП/Мощность'),
        ),
    ]