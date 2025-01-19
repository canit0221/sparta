from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile", views.profile, name="profile"),
    path("password_change/", views.password_change, name="password_change"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
]
