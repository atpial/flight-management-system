# mypy: ignore-errors

import uuid
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
import logging
from django.conf import settings
from datetime import timedelta, datetime, timezone
from utils.constants import USER_TYPE_CHOICES

logger = logging.getLogger("user")


class UserType(models.Model):
    user_type_id = models.AutoField(primary_key=True)
    user_type_name = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user_type_name


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.role_name

    def get_assigned_users(self):
        return Users.objects.filter(userrole__role_id=self, userrole__is_active=True)


class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role_id = models.ForeignKey(
        "Roles",
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return Roles.objects.get(id=self.role_id).role_name


class Users(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=False, blank=False)
    user_type = models.ForeignKey("UserType", on_delete=models.CASCADE, null=True)
    user_role = models.ManyToManyField("UserRole")

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def assign_role(self, role):
        if isinstance(role, Roles):
            UserRole.objects.get_or_create(user_id=self, role_id=role)
        elif isinstance(role, str):
            role_obj = Roles.objects.get(role_name=role)
            UserRole.objects.get_or_create(user_id=self, role_id=role_obj)
        else:
            raise ValueError("Invalid role type. Expected Roles instance or string.")

    def has_role(self, role):
        user_role = self.user_role.filter(role_id=role, user_id=self)
        print(user_role.query)
        return user_role.exists()

    def get_assigned_roles(self):
        return Roles.objects.filter(userrole__user_id=self, userrole__is_active=True)
