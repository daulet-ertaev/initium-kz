from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'post/home.html', context)


def about(request):
    return render(request, 'post/about.html', {'title': 'About'})