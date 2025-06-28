from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests

apiURL = 'http://localhost:8000/api/v1'

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

    response = requests.get(f'{apiURL}/posts')
    if response.status_code == 200:
        posts = response.json()

    context = {
        'posts': posts,
        'user': request.user,
        'username': request.session.get('username',''),
    }
    return render(request, 'index.html', context) 


@login_required(login_url='error_403')
def newpost(request):
    if request.method == 'POST':
        post = {}
        return redirect('index')
    return render(request, 'newpost.html')


def viewpost(request):
    post_id = request.GET.get('id')
    response = requests.get(f'{apiURL}/posts/{post_id}')
    if response.status_code == 200:
        posts = response.json()
    context = {
        'post': posts[0]
    }
    return render(request, 'viewpost.html', context)

@login_required(login_url='error_403')
def editpost(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        post = {}
        return redirect('index')
    post = {}
    context = {
        'post': post
    }
    return render(request, 'editpost.html', context)


@login_required(login_url='error_403')
def deletepost(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        post = {}
        return redirect('index')
    post_id = request.GET.get('id')
    post = {}
    context = {
        'post': post
    }
    return render(request, 'deletepost.html', context)
