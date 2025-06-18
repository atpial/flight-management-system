from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Airline
from .forms import AirlineForm


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
            return redirect("airlines:list")
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
            return redirect("airlines:list")
        return render(request, "airlines/form.html", {"form": form, "airline": airline})


class AirlineDeleteView(View):
    def get(self, request, pk):
        airline = get_object_or_404(Airline, pk=pk)
        return render(request, "airlines/confirm_delete.html", {"airline": airline})

    def post(self, request, pk):
        airline = get_object_or_404(Airline, pk=pk)
        airline.delete()
        return redirect("airlines:list")
