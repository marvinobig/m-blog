from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from.forms import CreatePostForm

# Create your views here.
@login_required
def dashboardView(request):
    user = request.user
    userPosts = user.posts.all()
    context = {"user": user, "userPosts": userPosts}

    return render(request, "dashboard.html", context)

@login_required
def allPostsView(request):
    posts = Post.objects.all()
    pass

@login_required
def createPostView(request):
    if request.method == "POST":
        pass
    else:
        form = CreatePostForm()
        context = {"form": form}

        return render(request, "new.html", context)