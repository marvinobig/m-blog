from django.urls import path
from . import views

urlpatterns = [
    path("", views.allPostsView, name="all"),
    path("dashboard/<int:userId>", views.dashboardView, name="dashboard"),
    path("new", views.createPostView, name="new"),
]