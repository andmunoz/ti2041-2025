from django.shortcuts import render, redirect
from .models import Post, Tag, Category

# Create your views here.
def index(request):
    posts = Post.objects.filter(active_post=True).order_by('publish_date')
    print(posts)
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context) 


def newpost(request):
    if request.method == 'POST':
        post = Post(
            title = request.POST.get('title'),
            content = request.POST.get('content')
        )
        post.save()
        return redirect('index')
    return render(request, 'newpost.html')


def viewpost(request):
    post_id = request.GET.get('id')
    post = Post.objects.get(id=post_id)
    tags = Tag.objects.filter(post__id=post_id)
    context = {
        'post': post,
        'tags': tags,
    }
    print(post)
    return render(request, 'viewpost.html', context)


def editpost(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('index')
    post_id = request.GET.get('id')
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'editpost.html', context)


def deletepost(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)
        post.active_post = False
        post.save()
        return redirect('index')
    post_id = request.GET.get('id')
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'deletepost.html', context)
