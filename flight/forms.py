from django import forms
from .models import Airline, Airport, Flight


class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = ["name", "code", "country", "description"]


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ["name", "code", "city", "country"]


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = [
            "flight_number",
            "airline",
            "departure_airport",
            "arrival_airport",
            "departure_time",
            "arrival_time",
            "duration",
            "price",
        ]
        widgets = {
            "departure_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "arrival_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class FlightSearchForm(forms.Form):
    flight_number = forms.CharField(
        label="Flight Number",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "e.g. F123"}),
    )
    airline = forms.ModelChoiceField(
        queryset=Airline.objects.all(), required=False, empty_label="Any Airline"
    )
    destination = forms.CharField(
        label="Destination",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter destination (e.g., USA, New York)"}
        ),
    )
