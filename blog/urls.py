from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail,
         name="post-detail-page")  # posts/my-first-post
]
