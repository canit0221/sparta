from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    # 프로필 이미지
    proifle_image = models.ImageField(upload_to="profile_image", blank=True, null=True)
    # 소개글
    bio = models.TextField(max_length=500, blank=True, null=True)
