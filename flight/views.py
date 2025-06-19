from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Airline, Airport
from .forms import AirlineForm, AirportForm


class AirlineListView(View):
    def get(self, request):
        airlines = Airline.objects.all()
        return render(request, "airlines/list.html", {"airlines": airlines})


class AirlineCreateView(View):
    def get(self, request):
        form = AirlineForm()
        return render(request, "airlines/form.html", {"form": form})

    def post(self, request):
        form = AirlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flight:airlines_list")
        return render(request, "airlines/form.html", {"form": form})


class AirlineUpdateView(View):
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


class AirlineDeleteView(View):
    def get(self, request, pk):
        airline = get_object_or_404(Airline, pk=pk)
        return render(request, "airlines/confirm_delete.html", {"airline": airline})

    def post(self, request, pk):
        airline = get_object_or_404(Airline, pk=pk)
        airline.delete()
        return redirect("flight:airlines_list")


class AirportListView(View):
    def get(self, request):
        airports = Airport.objects.all()
        return render(request, "airport/list.html", {"airports": airports})


class AirportCreateView(View):
    def get(self, request):
        form = AirportForm()
        return render(request, "airport/form.html", {"form": form})

    def post(self, request):
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flight:airports_list")
        return render(request, "airport/form.html", {"form": form})


class AirportUpdateView(View):
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


class AirportDeleteView(View):
    def get(self, request, pk):
        airport = get_object_or_404(Airport, pk=pk)
        return render(request, "airport/confirm_delete.html", {"airport": airport})

    def post(self, request, pk):
        airport = get_object_or_404(Airport, pk=pk)
        airport.delete()
        return redirect("flight:airports_list")
