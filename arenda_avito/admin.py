from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path

from .models import ArendaCar


@admin.register(ArendaCar)
class CarAdmin(admin.ModelAdmin):
    list_display = ('taxopark', 'cars', 'price', 'schedule', 'description', 'placement_date')# 'link', )

    change_list_template = "admin/model_change_list.html"

    #def get_urls(self):
    #    urls = super(CarAdmin, self).get_urls()
    #    custom_urls = [
    #        path('^import/$', self.process_import, name='process_import'), ]
    #    return custom_urls + urls
#
#
    #def process_import(self):
    #    print('hello_world')

