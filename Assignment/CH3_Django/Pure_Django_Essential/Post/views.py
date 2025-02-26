import re
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post, Comment, Like
from django.db.models import Count
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

"""
이 모듈은 Post 모델과 관련된 뷰 함수들을 정의합니다.

함수들:
- post_list(request): 모든 Post 객체를 리스트로 보여주는 뷰 함수입니다.
- post_detail(request, pk): 주어진 pk에 해당하는 Post 객체의 상세 정보를 보여주는 뷰 함수입니다.
- post_create(request): 새로운 Post 객체를 생성하는 뷰 함수입니다.
- post_update(request, pk): 주어진 pk에 해당하는 Post 객체를 업데이트하는 뷰 함수입니다.
"""


# Create your views here.
def post_list(request):
    sort_by = request.GET.get("sort", "pk")
    if sort_by == "likes":
        posts = Post.objects.annotate(like_count=Count("likes")).order_by(
            "-like_count", "-pk"
        )
    elif sort_by == "comments":
        posts = Post.objects.annotate(comment_count=Count("comments")).order_by(
            "-comment_count", "-pk"
        )
    else:
        posts = Post.objects.all().order_by("-pk")  # 모든 Post 객체를 가져옵니다.
    context = {"posts": posts}  # 컨텍스트에 posts를 추가합니다.
    return render(request, "Post/post_list.html", context)  # 템플릿을 렌더링합니다.


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)  # 주어진 pk로 Post 객체를 가져옵니다.
    form = CommentForm()  # 댓글 작성 폼을 생성합니다.
    context = {
        "post": post,
        "form": form,
        "profile_url": reverse("User:profile", args=[post.author.id]),
    }  # 컨텍스트에 post와 form을 추가합니다.
    return render(request, "Post/post_detail.html", context)  # 템플릿을 렌더링합니다.


@login_required  # 로그인이 필요합니다.
def post_create(request):
    if request.method == "POST":  # POST 요청인지 확인합니다.
        form = PostForm(request.POST)  # 제출된 데이터를 사용하여 폼을 생성합니다.
        if form.is_valid():  # 폼이 유효한지 확인합니다.
            post = form.save(
                commit=False
            )  # Post 객체를 저장하되, 아직 커밋하지 않습니다.
            post.author = request.user  # 현재 사용자를 작성자로 설정합니다.
            post.save()  # Post 객체를 저장합니다.
            return redirect("Post:post_list")  # 포스트 리스트로 리디렉션합니다.
    else:
        form = PostForm()  # GET 요청인 경우 빈 폼을 생성합니다.

    return render(
        request, "Post/post_form.html", {"form": form}
    )  # 템플릿을 렌더링합니다.


@login_required  # 로그인이 필요합니다.
def post_update(request, pk):
    post = Post.objects.get(pk=pk)  # 주어진 pk로 Post 객체를 가져옵니다.
    if request.method == "POST":  # POST 요청인지 확인합니다.
        form = PostForm(
            request.POST, instance=post
        )  # 제출된 데이터로 PostForm을 생성합니다.
        if form.is_valid():  # 폼이 유효한지 확인합니다.
            form.save()  # Post 객체를 저장합니다.
            return redirect(
                "Post:post_detail", pk=post.pk
            )  # 상세 페이지로 리디렉션합니다.
    else:
        form = PostForm(
            instance=post
        )  # POST가 아닐 경우, 기존 Post 객체로 폼을 생성합니다.
    context = {"form": form, "post": post}  # 컨텍스트에 폼과 포스트를 추가합니다.

    return render(request, "Post/post_form.html", context)  # 템플릿을 렌더링합니다.


@require_POST  # POST 요청만 허용합니다.
def post_delete(request, pk):
    if request.user.is_authenticated:  # 사용자가 인증되어 있으면
        post = Post.objects.get(pk=pk)  # 주어진 pk로 Post 객체를 가져옵니다.
        post.delete()  # Post 객체를 삭제합니다.
    return redirect("Post:post_list")  # 포스트 리스트로 리디렉션합니다.


@login_required
@require_POST
def toggle_like(request, post_id):
    post = Post.objects.get(pk=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect("Post:post_detail", pk=post.pk)


@login_required
@require_POST
def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        return redirect("Post:post_detail", pk=post.pk)
    return redirect("Post:post_detail", pk=post.pk)
