from django.shortcuts import render, HttpResponse, redirect

from cmsapp.forms import PostForm
from .models import Post
from django.utils.text import slugify
from django.contrib import messages


# Create your views here.
def index(request):
    posts = Post.objects.all()
    contex = {"post": posts}
    return render(request, "index.html", contex)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:3]
    contex = {"post": post, "posts": posts}
    return render(request, "detail.html", contex)


def CreatePost(request):
    profile=request.user.userprofile
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer=profile
            post.slug = slugify(post.title)
            post.save()
            messages.info(request,"Article created successfully")
        else:
            messages.info(request,"Article not created successfully")
            return redirect("create")
    contex = {"form": form}
    return render(request, "index.html", contex)


def UpdatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request,"Article updated successfully")
            
            return redirect("detail", slug=post.slug)
    contex = {"form": form}
    return render(request, "create.html", contex)


def DeletePost(request,slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    contex = {"form": form}
    if request.method == "POST":
        post.delete()
        messages.info(request,"Article deleted successfully")
        
        return redirect("index")
    return render(request, "delete.html", contex)
