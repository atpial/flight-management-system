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
]
