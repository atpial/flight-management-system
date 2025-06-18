from django import forms
from .models import Airline


class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = ["name", "code", "country", "description"]
