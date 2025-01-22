from django.urls import path
from . import views

app_name = "Post"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("create/", views.post_create, name="post_create"),
    path("update/<int:pk>/", views.post_update, name="post_update"),
    path("delete/<int:pk>/", views.post_delete, name="post_delete"),
    path("<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path("<int:post_id>/toggle_like/", views.toggle_like, name="toggle_like"),
]
