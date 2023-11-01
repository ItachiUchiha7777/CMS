from django.shortcuts import render,HttpResponse
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    contex = {"post": posts}
    return render(request, "index.html", contex)


def detail(request,slug):
    post=Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    contex = {"post":post,"posts":posts}
    return render(request, "detail.html", contex)
 
