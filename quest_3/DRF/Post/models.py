from django.db import models
from config import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )  # Post 모델과 1:N 관계, Post 객체가 삭제되면 Comment 객체도 삭제
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )  # Post 모델과 1:N 관계, Post 객체가 삭제되면 Like 객체도 삭제
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post", "user")  # post와 user의 조합은 유일해야 한다.

    def __str__(self):
        return f"{self.user} likes {self.post}"
