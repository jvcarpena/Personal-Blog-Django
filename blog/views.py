from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def index(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    # list comprehension using next function.
    # post_to_show = next(post for post in all_posts if post['slug'] == slug)
    post_to_show = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": post_to_show,
        "post_tags": post_to_show.tag.all()
    })
