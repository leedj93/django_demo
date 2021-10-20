from django.shortcuts import render

from blog.models import Post
# Create your views here.

def blog_home(request):


    return render(request, "blog/index.html")

def blog_post(request):
    return render(request, "blog/post.html")

def blog_create(request):

    new_post = Post()
    new_post.title = "title from views.py"
    new_post.content = "content from views.py"
    new_post.likes = 0
    new_post.save()

    return render(request, "blog/create.html")
