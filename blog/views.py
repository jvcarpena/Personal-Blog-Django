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
    def is_stored_post(self, request, post_id):
        """This is a helper function for the read-later feature."""
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else: 
            is_saved_for_later = False
        return is_saved_for_later


    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        return render(request, "blog/post-detail.html", {
            "post": post,
            "post_tags": post.tag.all(),  # This will get the all tags.
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),  # To fetch all the comments related to that post using the related name.
            "saved_for_later": self.is_stored_post(request, post.id)
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
            "comments": post.comments.all().order_by("-id"),
            'saved_for_later': self.is_stored_post(request, post.id)
        })


# VIEW FOR READ_LATER FEATURE
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts == None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        
        else:
            posts = Post.objects.filter(id__in=stored_posts)  # use special modifire in that checks the id in a list.
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored-post.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts == None:
            stored_posts = []
        
        # if stored_posts is not None.
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
            
        request.session["stored_posts"] = stored_posts  # To store the post in session.
        
        return HttpResponseRedirect("/")
