from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts is a list of dictionaries

"""
posts = [
    {
        "author": "Jane Doe",
        "title": "Blog post 1",
        "content": "testtesttest",
        "date_posted": "August 27, 2028",
    },
    {
        "author": "Ben Doe",
        "title": "Blog post 2",
        "content": "testtesttest",
        "date_posted": "August 28, 2028",
    },
]
"""


def home(request):
    context = {"posts": Post.objects.all(), "title": "TestContextTitle"}
    # return HttpResponse('<h1>Welcome to the Blog Home Page</h1>')
    return render(
        request, "blog/home.html", context
    )  # use template in blog/template/blog/


def about(request):
    # return HttpResponse("<h1>About the Blog</h1>")
    return render(
        request, "blog/about.html", {"title": "About"}
    )  # use template in blog/template/blog/
