from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(),
         name="post-detail-page"),  # posts/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
