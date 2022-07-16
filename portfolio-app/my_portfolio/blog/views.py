from django.shortcuts import render
from .models import Blog


def index(request):
    projects = Blog.objects.all()
    return render(request, 'blog/index.html', {'projects': projects})
