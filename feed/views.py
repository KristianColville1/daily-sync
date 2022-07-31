from django.shortcuts import get_object_or_404, render
from django.views import View, generic
from posts.models import Post
from posts.forms import PostForm


class FeedViewIndex(View):
    """
    FeedView class
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(status=1).order_by("-created_on")
        form = PostForm()
        context = {
            'posts': post,
            'form': form
        }
        return render(request, 'feed/index.html', context)

    def post(self, request, *args, **kwargs):
        post = Post.objects.filter(status=1).order_by("-created_on")
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

class FeedViewPost(View):
    """
    FeedViewPost class
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        form = PostForm()
        context = {'posts': post, 'form': form}
        return render(request, 'posts/view_post.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        form = PostForm()
        context = {'posts': post, 'form': form}

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.status = 1
            post_form.save()
        return render(request, 'posts/index.html', context)