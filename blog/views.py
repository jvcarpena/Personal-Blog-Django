from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    pass
