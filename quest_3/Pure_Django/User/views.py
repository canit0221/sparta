from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method == "POST":  # POST 요청인지 확인합니다.
        form = AuthenticationForm(
            request, request.POST
        )  # 제출된 데이터로 AuthenticationForm을 생성합니다.
        if form.is_valid():  # 폼이 유효한지 확인합니다.
            auth_login(request, form.get_user())  # 사용자를 로그인합니다.
            return redirect("Post:post_list")  # 포스트 리스트로 리디렉션합니다.
    else:
        form = AuthenticationForm()  # AuthenticationForm 인스턴스를 생성합니다.
    context = {"form": form}  # 컨텍스트에 form을 추가합니다.
    return render(request, "User/login.html", context)  # 템플릿을 렌더링합니다.


@require_POST  # POST 요청만 허용합니다.
def logout(request):
    if request.user.is_authenticated:  # 사용자가 인증되어 있으면 로그아웃합니다.
        auth_logout(request)
    return redirect("Post:post_list")  # 포스트 리스트로 리디렉션합니다.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("User:login")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "User/signup.html", context)


@login_required  # 로그인이 필요합니다.
def profile(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("User:profile")  # 프로필 페이지로 리디렉션합니다.
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(
        request, "User/profile.html", context
    )  # 프로필 템플릿을 렌더링합니다.


@login_required  # 로그인이 필요합니다.
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("User:profile")  # 프로필 페이지로 리디렉션합니다.
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "User/password_change.html", context)
