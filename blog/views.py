from django.shortcuts import render
from datetime import date
from .models import Post
# Create your views here.

all_posts = [
    
]


def get_date(post):
    return post['date']


def index(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    # list comprehension using next function.
    # post_to_show = next(post for post in all_posts if post['slug'] == slug)
    post_to_show = None
    for item in all_posts:
        if item['slug'] == slug:
            post_to_show = item
    return render(request, "blog/post-detail.html", {
        "post": post_to_show
    })
