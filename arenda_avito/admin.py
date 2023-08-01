from django.contrib import admin

from .models import ArendaCar


@admin.register(ArendaCar)
class CarAdmin(admin.ModelAdmin):
    list_display = ('taxopark', 'cars', 'price', 'schedule')
                    #, 'placement_date', 'komission_park','usloviya_vivoda_sredstv',)# 'link', 'description' )

    change_list_template = "admin/model_change_list.html"



