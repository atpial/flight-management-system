from django import forms
from .models import Airline, Airport


class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = ["name", "code", "country", "description"]


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ["name", "code", "city", "country"]
