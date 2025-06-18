from django.urls import path
from .views import HomeView, LoginView, RegisterView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("register/<str:user_type>/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
