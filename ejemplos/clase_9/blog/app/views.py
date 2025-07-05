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
        post = {
            'title': request.POST['title'],
            'text': request.POST['content'],
            'author_id': request.user.id,
            'category_id': 1,
            'publish_date': '2025-07-05',
            'status': True,
        }
        response = requests.post(f'{apiURL}/posts/', json=post)
        return redirect('index')
    return render(request, 'newpost.html')


def viewpost(request):
    post_id = request.GET.get('id')
    response = requests.get(f'{apiURL}/posts/{post_id}')
    if response.status_code == 200:
        post = response.json()
    context = {
        'post': post
    }
    return render(request, 'viewpost.html', context)


@login_required(login_url='error_403')
def editpost(request):
    if request.method == 'POST':
        post_id = request.POST['id']
        response = requests.get(f'{apiURL}/posts/{post_id}')
        if response.status_code == 200:
            post = response.json()
            post['title'] = request.POST['title']
            post['text'] = request.POST['content']
            response = requests.put(f'{apiURL}/posts/{post_id}', json=post)

    post_id = request.GET.get('id')
    response = requests.get(f'{apiURL}/posts/{post_id}')
    if response.status_code == 200:
        post = response.json()
    context = {
        'post_id': post_id,
        'post': post,
    }
    return render(request, 'editpost.html', context)


@login_required(login_url='error_403')
def deletepost(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        response = requests.delete(f'{apiURL}/posts/{post_id}')
        return redirect('index')

    post_id = request.GET.get('id')
    context = {
        'post_id': post_id
    }
    return render(request, 'deletepost.html', context)
