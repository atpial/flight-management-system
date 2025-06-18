import time
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from user.models import Users, UserType


class UserRegistrationForm(forms.Form):
    USER_TYPE_CHOICES = [("Admin", "Admin"), ("Customer", "Customer")]

    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
            )
        ],
    )
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Users.objects.filter(email=email).exists():
            print("Email already exists.")
            raise ValidationError("Email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        validate_password(password)
        return password

    def clean(self):
        cleaned_data = super().clean()

        user_type = cleaned_data.get("user_type")

        if user_type not in dict(self.USER_TYPE_CHOICES):
            raise ValidationError({"user_type": "Invalid user type."})

        return cleaned_data

    def save(self):
        data = self.cleaned_data
        print("Saving user with data:", data)
        timestamp = int(time.time())
        unique_username = f"{data['username']}_{timestamp}"

        # Get or create user type
        user_type_obj, _ = UserType.objects.get_or_create(
            user_type_name=data["user_type"],
            defaults={"description": f"{data['user_type']} account"},
        )

        is_admin = data["user_type"] == "Admin"

        user = Users(
            username=unique_username,
            email=data["email"],
            phone=data["phone"],
            user_type=user_type_obj,
            is_staff=is_admin,
            is_superuser=is_admin,
        )
        user.set_password(data["password"])
        user.save()
        return user
