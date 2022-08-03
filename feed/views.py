from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib import messages
from posts.models import Post
from posts.forms import PostForm


class FeedViewIndex(View):
    """
    FeedView class
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(status=1).order_by("-created_on")
        form = PostForm()
        context = {'posts': post, 'form': form}
        return render(request, 'feed/index.html', context)

    def post(self, request, *args, **kwargs):
        post = Post.objects.filter(status=1).order_by("-created_on")
        form = PostForm()
        context = {'posts': post, 'form': form}
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.status = 1
            post_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your post has been successfully submitted')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Oops something has went wrong, please try again!')
        return render(request, 'feed/index.html', context)


class FeedViewPost(View):
    """
    FeedViewPost class
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        form = PostForm()
        context = {'post': post, 'form': form}
        return render(request, 'posts/view_post.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        form = PostForm()
        context = {'post': post, 'form': form}

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.status = 1
            post_form.save()
        return render(request, 'posts/index.html', context)
