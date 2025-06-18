from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from user.models import Users
from django.views import View
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class RegisterView(View):
    def get(self, request, user_type):
        form = UserRegistrationForm()
        return render(request, "register.html", {"form": form, "user_type": user_type})

    def post(self, request, user_type):
        data = request.POST.copy()
        data["user_type"] = user_type.capitalize()
        form = UserRegistrationForm(data)
        if form.is_valid():
            form.save()
            # Redirect to login or homepage after successful registration
            return redirect("login")
        return render(request, "register.html", {"form": form, "user_type": user_type})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return render(
                request,
                "login.html",
                {"error": "Email and password are required."},
            )

        try:
            user = Users.objects.get(email=email)
            auth_user = authenticate(username=user.username, password=password)

            if auth_user is None:
                return render(request, "login.html", {"error": "Invalid credentials."})

            login(request, auth_user)
            return redirect("home")  # or redirect to dashboard/profile page
        except Users.DoesNotExist:
            return render(request, "login.html", {"error": "User not found."})
        except Exception as e:
            return render(request, "login.html", {"error": str(e)})


@method_decorator(login_required, name="dispatch")
class HomeView(View):
    def get(self, request):
        return render(request, "home.html", {"user": request.user})
