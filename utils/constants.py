# mypy: ignore-errors

from enum import Enum
from django.conf import settings
import logging


USER_TYPE_CHOICES = [
    ("Admin", "ADMIN"),
    ("Customer", "CUSTOMER"),
]
