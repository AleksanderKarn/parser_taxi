from os import path

from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    class Meta:
        model = Report

    list_display = ('mark', 'model', 'average_price',)
