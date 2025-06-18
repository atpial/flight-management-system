from django.urls import path
from .views import (
    AirlineListView,
    AirlineCreateView,
    AirlineUpdateView,
    AirlineDeleteView,
)

app_name = "airlines"

urlpatterns = [
    path("", AirlineListView.as_view(), name="list"),
    path("create/", AirlineCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", AirlineUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", AirlineDeleteView.as_view(), name="delete"),
]
