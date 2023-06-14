from django import forms

from list_auto_avito.models import CarListAvito


class CarListAvitoForm(forms.ModelForm):
    class Meta:
        model = CarListAvito
        fields = ('mark', 'model', 'year_from', 'mileage', 'price', 'body_type', 'volume',)