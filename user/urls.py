from django.urls import path
from .views import HomeView, LoginView, LogoutView, RegisterView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("register/<str:user_type>/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
