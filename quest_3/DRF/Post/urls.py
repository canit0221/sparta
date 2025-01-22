from django.urls import URLPattern, path
from . import views

app_name = "Post"

urlpatterns = [
    path("", views.PostListAPIView.as_view(), name="Post_list"),
    path("<int:pk>/", views.PostDetailAPIView.as_view(), name="Post_detail"),
]
