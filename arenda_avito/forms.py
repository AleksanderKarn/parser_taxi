from django import forms

from arenda_avito.models import ArendaCar


class ArendaCarForm(forms.ModelForm):
    class Meta:
        model = ArendaCar
        fields = ('cars', 'price', 'taxopark', 'link', 'description', 'schedule', 'placement_date', 'komission_park'
                  , 'usloviya_vivoda_sredstv')
