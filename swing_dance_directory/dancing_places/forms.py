from django import forms
from .models import Spot

class SpotForm(forms.ModelForm):
    class Meta:
        model = Spot
        fields = ['name', 'description','address']
