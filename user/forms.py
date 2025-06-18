from django import forms
from .serializers import UserSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        serializer = UserSerializer(data=cleaned_data)
        try:
            serializer.is_valid(raise_exception=True)
        except DRFValidationError as e:
            # Convert DRF validation errors to Django form errors
            for field, errors in e.detail.items():
                for error in errors:
                    self.add_error(field, error)
        return cleaned_data

    def save(self):
        serializer = UserSerializer(data=self.cleaned_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return user
