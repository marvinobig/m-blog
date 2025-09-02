from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
@login_required
def dashboardView(request, userId):
    user = get_object_or_404(User, id=userId)
    userPosts = user.posts.all()
    context = {"user": user, "userPosts": userPosts}

    return render(request, "dashboard.html", context)

@login_required
def allPostsView(request):
    posts = Post.objects.all()
    pass

@login_required
def createPostView(request):
    pass