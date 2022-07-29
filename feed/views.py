from django.shortcuts import render
from django.views import View, generic
from posts.models import Post
from posts.forms import PostForm


class FeedView(View):
    """
    FeedView class
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(status=1)
        form = PostForm()
        context = {
            'posts': post,
            'form': form
        }
        return render(request, 'feed/index.html', context)
    
    def post(self, request, *args, **kwargs):
        post = Post.objects.filter(status=1)
        form = PostForm()
        context = {
            'posts': post,
            'form': form
        }
        
        post_form = PostForm(data=request.POST)
        
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.status = 1
            post_form.save()
        return render(request, 'feed/index.html', context)