from django.contrib import admin


from .models import CarList


@admin.register(CarList)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'year_from', 'mileage', 'body_type', 'volume', 'price',)

    change_list_template = "admin/model_change_list.html"