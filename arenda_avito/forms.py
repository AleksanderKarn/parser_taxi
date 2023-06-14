from django import forms

from arenda_avito.models import ArendaCar


class ArendaCarForm(forms.ModelForm):
    class Meta:
        model = ArendaCar
        fields = ('mark', 'model','price', 'link')