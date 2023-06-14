
from django import forms

from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('id', 'mark', 'model', 'year_from', 'mileage_from', 'mileage_to',)