from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, View
from .models import Post
from .forms import CommentForm
# Create your views here.


class HomeView(View):
    def get(self, request):
        latest_post = Post.objects.all().order_by("-date")[:3]
        return render(request, "blog/index.html", {
            "posts": latest_post
        })


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    ordering = ["-date"]
    context_object_name = "posts"


class PostDetailView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post-detail.html", {
            "post": post,
            "post_tags": post.tag.all(),  # This will get the all tags.
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")  # To fetch all the comments related to that post using the related name.
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            # Because we exclude the post in the form.
            # So before saving it we need to get it.
            comment = comment_form.save(commit=False)  # will just create a model instance.
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        return render(request, "blog/post-detail.html", {
            "post": post,
            "post_tags": post.tag.all(),  # This will get the all tags.
            "comment_form": comment_form,  # prepopulated form if it is invalid.
            "comments": post.comments.all().order_by("-id")
        })
    