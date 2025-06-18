# mypy: ignore-errors


from rest_framework import serializers

from .models import Users, UserType
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
import time

from django.contrib.auth.hashers import check_password


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ["user_type_id", "user_type_name", "description"]


class UserSerializer(serializers.ModelSerializer):
    USER_TYPE_CHOICES = ["Admin", "Customer"]

    user_type = serializers.CharField()

    email = serializers.EmailField(required=True)
    phone = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
            )
        ]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = Users
        fields = ["user_id", "username", "email", "password", "phone", "user_type"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_user_type(self, value):
        """Ensure user_type is one of the allowed values."""
        if value not in self.USER_TYPE_CHOICES:
            raise serializers.ValidationError(
                f"Invalid user_type. Allowed values: {self.USER_TYPE_CHOICES}"
            )
        return value

    def validate_email(self, value):
        """Check if the email already exists."""
        if Users.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate(self, data):
        """Check for unknown fields."""
        if hasattr(self, "initial_data"):
            unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
            if unknown_keys:
                raise serializers.ValidationError(f"Got unknown fields: {unknown_keys}")
        return data

    def create(self, validated_data):
        print(f"validated_data: {validated_data}")
        timestamp = int(time.time())
        unique_username = f"{validated_data['username']}_{timestamp}"

        # Validate user_type
        user_type_name = validated_data.pop("user_type")

        if user_type_name not in self.USER_TYPE_CHOICES:
            raise serializers.ValidationError({"user_type": ["Invalid user type."]})

        user_type, created = UserType.objects.get_or_create(
            user_type_name=user_type_name,
            defaults={"description": f"{user_type_name} account"},
        )
        # Determine if the user should be an admin
        is_admin = user_type_name == "Admin"

        # Create user
        user = Users(
            username=unique_username,
            phone=validated_data["phone"],
            email=validated_data["email"],
            user_type=user_type,
            is_staff=is_admin,
            is_superuser=is_admin,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
