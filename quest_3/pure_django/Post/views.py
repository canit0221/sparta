from pickle import FALSE
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "Post/post_list.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, "Post/post_detail.html", context)


def post_create(request):
    if request.method == "POST":
        forms = PostForm(request.POST)
        if forms.is_valid():
            post = form.save(commit=FALSE)
            post.author = request.user
            post.save()
            return redirect("Post/post_list")
        else:
            form = PostForm()

    return render(request, "Post/post_create.html")
