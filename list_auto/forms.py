from django import forms

from list_auto.models import CarList


class CarListForm(forms.ModelForm):
    class Meta:
        model = CarList
        fields = ('mark', 'model', 'year_from', 'mileage', 'price', 'body_type', 'volume',)