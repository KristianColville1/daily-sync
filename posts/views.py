from django.shortcuts import render
from .models import Post


def get_posts(request):
    posts = Post.objects.all()
    context = {
      'posts': posts
    }
    return render(request, 'posts/index.html', context)
