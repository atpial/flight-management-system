from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import View
from .models import Airline, Airport, Flight
from .forms import AirlineForm, AirportForm, FlightForm, FlightSearchForm
from utils.mixins import AdminRequiredMixin


class AirlineListView(AdminRequiredMixin, View):
    def get(self, request):
        airlines = Airline.objects.all()
        return render(request, "airlines/list.html", {"airlines": airlines})


class AirlineCreateView(AdminRequiredMixin, View):
    def get(self, request):
        form = AirlineForm()
        return render(request, "airlines/form.html", {"form": form})

    def post(self, request):
        form = AirlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flight:airlines_list")
        return render(request, "airlines/form.html", {"form": form})


class AirlineUpdateView(AdminRequiredMixin, View):
    def get(self, request, pk):
        airline = get_object_or_404(Airline, pk=pk)
        form = AirlineForm(instance=airline)
        return render(request, "airlines/form.html", {"form": form, "airline": airline})

    def post(self, request, pk):
        airline = get_object_or_404(Airline, pk=pk)
        form = AirlineForm(request.POST, instance=airline)
        if form.is_valid():
            form.save()
            return redirect("flight:airlines_list")
        return render(request, "airlines/form.html", {"form": form, "airline": airline})


class AirlineDeleteView(AdminRequiredMixin, View):
    def get(self, request, pk):
        airline = get_object_or_404(Airline, pk=pk)
        return render(request, "airlines/confirm_delete.html", {"airline": airline})

    def post(self, request, pk):
        airline = get_object_or_404(Airline, pk=pk)
        airline.delete()
        return redirect("flight:airlines_list")


class AirportListView(AdminRequiredMixin, View):
    def get(self, request):
        airports = Airport.objects.all()
        return render(request, "airport/list.html", {"airports": airports})


class AirportCreateView(AdminRequiredMixin, View):
    def get(self, request):
        form = AirportForm()
        return render(request, "airport/form.html", {"form": form})

    def post(self, request):
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flight:airports_list")
        return render(request, "airport/form.html", {"form": form})


class AirportUpdateView(AdminRequiredMixin, View):
    def get(self, request, pk):
        airport = get_object_or_404(Airport, pk=pk)
        form = AirportForm(instance=airport)
        return render(request, "airport/form.html", {"form": form, "airport": airport})

    def post(self, request, pk):
        airport = get_object_or_404(Airport, pk=pk)
        form = AirportForm(request.POST, instance=airport)
        if form.is_valid():
            form.save()
            return redirect("flight:airports_list")
        return render(request, "airport/form.html", {"form": form, "airport": airport})


class AirportDeleteView(AdminRequiredMixin, View):
    def get(self, request, pk):
        airport = get_object_or_404(Airport, pk=pk)
        return render(request, "airport/confirm_delete.html", {"airport": airport})

    def post(self, request, pk):
        airport = get_object_or_404(Airport, pk=pk)
        airport.delete()
        return redirect("flight:airports_list")


class FlightListView(View):
    def get(self, request):
        flights = Flight.objects.all()
        return render(request, "flight/list.html", {"flights": flights})


class FlightCreateView(AdminRequiredMixin, View):
    def get(self, request):
        form = FlightForm()
        return render(request, "flight/form.html", {"form": form})

    def post(self, request):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flight:flights_list")
        return render(request, "flight/form.html", {"form": form})


class FlightUpdateView(AdminRequiredMixin, View):
    def get(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        form = FlightForm(instance=flight)
        return render(request, "flight/form.html", {"form": form, "flight": flight})

    def post(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect("flight:flights_list")
        return render(request, "flight/form.html", {"form": form, "flight": flight})


class FlightDeleteView(AdminRequiredMixin, View):
    def get(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        return render(request, "flight/confirm_delete.html", {"flight": flight})

    def post(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        flight.delete()
        return redirect("flight:flights_list")


class FlightSearchView(View):
    def get(self, request):
        form = FlightSearchForm(request.GET or None)
        flights = []

        if form.is_valid():
            flight_number = form.cleaned_data.get("flight_number")
            airline = form.cleaned_data.get("airline")
            destination = form.cleaned_data.get("destination")

            flights = Flight.objects.all()

            if flight_number:
                flights = flights.filter(flight_number__icontains=flight_number)
            if airline:
                flights = flights.filter(airline=airline)
            if destination:
                flights = flights.filter(
                    Q(arrival_airport__name__icontains=destination)
                    | Q(arrival_airport__country__icontains=destination)
                )

        return render(
            request, "flight/search_results.html", {"form": form, "flights": flights}
        )
