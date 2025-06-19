from django.urls import path
from .views import (
    AirlineListView,
    AirlineCreateView,
    AirlineUpdateView,
    AirlineDeleteView,
    AirportListView,
    AirportCreateView,
    AirportUpdateView,
    AirportDeleteView,
    FlightCreateView,
    FlightDeleteView,
    FlightListView,
    FlightSearchView,
    FlightUpdateView,
)

app_name = "flight"

urlpatterns = [
    # Airline URLs
    path("airlines/", AirlineListView.as_view(), name="airlines_list"),
    path("airlines/create/", AirlineCreateView.as_view(), name="airlines_create"),
    path("airlines/<int:pk>/edit/", AirlineUpdateView.as_view(), name="airlines_edit"),
    path(
        "airlines/<int:pk>/delete/", AirlineDeleteView.as_view(), name="airlines_delete"
    ),
    # Airport URLs
    path("airports/", AirportListView.as_view(), name="airports_list"),
    path("airports/create/", AirportCreateView.as_view(), name="airports_create"),
    path("airports/<int:pk>/edit/", AirportUpdateView.as_view(), name="airports_edit"),
    path(
        "airports/<int:pk>/delete/", AirportDeleteView.as_view(), name="airports_delete"
    ),
    # Flight URLs
    path("flights/", FlightListView.as_view(), name="flights_list"),
    path("flights/create/", FlightCreateView.as_view(), name="flights_create"),
    path("flights/<int:pk>/edit/", FlightUpdateView.as_view(), name="flights_edit"),
    path("flights/<int:pk>/delete/", FlightDeleteView.as_view(), name="flights_delete"),
    path("flights/search/", FlightSearchView.as_view(), name="flights_search"),
]
