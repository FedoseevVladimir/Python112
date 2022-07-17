from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'blog/home.html')


def index(request):
    projects = Blog.objects.all()
    return render(request, 'blog/index.html', {'projects': projects})


def price(request):
    return render(request, 'blog/price.html')


def feedback(request):
    return render(request, 'blog/feedback.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'blog/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'blog/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Такое имя пользователя уже существует'})
        else:
            return render(request, 'blog/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'blog/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'blog/loginuser.html', {'form': AuthenticationForm(), 'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('index')