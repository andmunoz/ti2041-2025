from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Tag, Category

# Create your views here.
def error403(request):
    return render(request, 'error403.html')


def index(request):
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'login':
            username = request.POST['username']
            password = request.POST['password']
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                request.session['username'] = username

        elif action == 'logout':
            logout(request)
            request.session.set_expiry(-1)

    posts = Post.objects.filter(active_post=True).order_by('publish_date')

    context = {
        'posts': posts,
        'user': request.user,
        'username': request.session.get('username',''),
    }
    return render(request, 'index.html', context) 


@login_required(login_url='error_403')
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


@login_required(login_url='error_403')
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


@login_required(login_url='error_403')
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
