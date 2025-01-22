from django.urls import path

"""
이 모듈은 Django URL 패턴을 정의합니다.

경로:
- "posts/": PostListAPIView를 호출하여 모든 게시물을 나열합니다.
- "posts/<int:pk>/": PostDetailAPIView를 호출하여 특정 게시물의 세부 정보를 표시합니다.
- "posts/<int:post_pk>/comments/": CommentListAPIView를 호출하여 특정 게시물의 모든 댓글을 나열합니다.
- "comments/<int:comment_pk>/": CommentDetailAPIView를 호출하여 특정 댓글의 세부 정보를 표시합니다.
- "posts/<int:post_pk>/like/": LikeAPIView를 호출하여 특정 게시물에 좋아요를 추가합니다.

뷰:
- PostListAPIView: 게시물 목록을 처리하는 뷰입니다.
- PostDetailAPIView: 특정 게시물의 세부 정보를 처리하는 뷰입니다.
- CommentListAPIView: 특정 게시물의 댓글 목록을 처리하는 뷰입니다.
- CommentDetailAPIView: 특정 댓글의 세부 정보를 처리하는 뷰입니다.
- LikeAPIView: 특정 게시물에 좋아요를 추가하는 뷰입니다.
"""
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
    LikeAPIView,
)

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail"),
    path(
        "posts/<int:post_pk>/comments/",
        CommentListAPIView.as_view(),
        name="comment-list",
    ),
    path(
        "comments/<int:comment_pk>/",
        CommentDetailAPIView.as_view(),
        name="comment-detail",
    ),
    path("posts/<int:post_pk>/like/", LikeAPIView.as_view(), name="like"),
]
