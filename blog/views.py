from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Post
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


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"

    # To fetch the tag on the current detail provided by DetailView Class.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tag.all()
        return context
