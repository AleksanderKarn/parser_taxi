from django.contrib import admin
from django.db.models import QuerySet

from list_auto_avito.models import CarListAvito
from .arenda_parser.parser_cen_arendi import _main
from .models import Car
from .parser.parser_auto_ru import main
from .parser_avito.parser_avito_ru import _input


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'year_from', 'mileage_from', 'mileage_to',)
    actions = ['parsing', 'avito_parser', 'arenda_parser',]

    @admin.action(description='Получить список выбранных автомобилей с Avto.ru')
    def parsing(self, request, qs: QuerySet):
        main()

    @admin.action(description='Получить список авто с AVITO')
    def avito_parser(self, request, qs: QuerySet):
        CarListAvito.objects.all().delete()
        _input()

    @admin.action(description='Получить данные Аренды авто с Авито')
    def arenda_parser(self, request, qs: QuerySet):
        _main()









