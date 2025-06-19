from django.db import models


class Airline(models.Model):
    """Airline model to represent an airline."""

    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(
        max_length=10, unique=True
    )  # Code (e.g., 'AA' for American Airlines)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Airport(models.Model):
    """Airport model to represent an airport."""

    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(
        max_length=10, unique=True
    )  # Code (e.g., 'JFK' for John F. Kennedy International Airport)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures"
    )
    arrival_airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals"
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} ({self.airline.name})"
