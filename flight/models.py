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
