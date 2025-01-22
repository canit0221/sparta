import re
from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = (
            "post",
            "author",
        )  # post와 author는 자동으로 설정되므로 수정할 수 없도록 설정

    def to_representation(self, instance):
        data = super().to_representation(instance)  # 기존 직렬화된 데이터를 가져온다.
        data.pop("post")  # post 필드 삭제
        return data  # 수정된 데이터 반환


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = (
            "post",
            "user",
        )  # post와 user는 자동으로 설정되므로 수정할 수 없도록 설정

    def to_representation(self, instance):
        data = super().to_representation(instance)  # 기존 직렬화된 데이터를 가져온다.
        data.pop("post")  # post 필드 삭제
        return data  # 수정된 데이터 반환


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(
        source="comment_set", many=True, read_only=True
    )  # comment_set을 CommentSerializer로 직렬화한다.
    comments_count = serializers.IntegerField(
        source="comment_set.count", read_only=True
    )  # comment_set의 개수를 세어준다.
    likes = LikeSerializer(many=True, read_only=True)  # LikeSerializer로 직렬화한다.
    likes_count = serializers.IntegerField(
        source="like_set.count", read_only=True
    )  # like_set의 개수를 세어준다.

    def to_representation(self, instance):
        data = super().to_representation(instance)  # 기존 직렬화된 데이터를 가져온다.
        data["author"] = instance.author.username  # author 필드에 username을 넣는다.
        return data  # 수정된 데이터 반환
