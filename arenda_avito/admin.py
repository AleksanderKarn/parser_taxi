from django.contrib import admin


from .models import ArendaCar


@admin.register(ArendaCar)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'price', 'link',)