from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("user_profile", views.user_profile, name="user_profile"),
    path("password_change/", views.password_change, name="password_change"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
]
