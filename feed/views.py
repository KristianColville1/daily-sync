from django.shortcuts import get_object_or_404, render
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q
from profiles.models import Profile
from posts.models import Post
from posts.forms import PostForm, CommentForm


class FeedViewIndex(View):
    """
    FeedView class
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(
            Q(author=request.user) |
            Q(author__profile__in=request.user.profile.friends.all()) |
            Q(author__profile__in=request.user.profile.follows.all())
        )
        profiles = Profile.objects.exclude(
            Q(user__profile__in=request.user.profile.friends.all()) |
            Q(user__profile__in=request.user.profile.follows.all())
        )
        post_paginator = Paginator(post, 9)
        page_number = request.GET.get('page')
        post_obj = post_paginator.get_page(page_number)
        profile_paginator = Paginator(profiles, 3)
        profile_obj = profile_paginator.get_page(page_number)
        context = {
            'profile': request.user.profile,
            'profiles': profile_obj,
            'posts': post_obj,
            'comment_form': CommentForm(),
            'form': PostForm()
        }
        return render(request, 'feed/index.html', context)

    def post(self, request, *args, **kwargs):
        post = Post.objects.filter(status=1).order_by("-created_on")
        paginator = Paginator(post, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = PostForm()
        context = {
            'posts': page_obj,
            'comment_form': CommentForm(),
            'form': form,
            'profile': request.user.profile
        }
        return render(request, 'feed/index.html', context)


class FeedViewPost(View):
    """
    FeedViewPost class
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        context = {
            'post': post,
            'comments': comments,
            'comment_form': CommentForm(),
            'profile': request.user.profile,
        }
        return render(request, 'posts/view_post.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        context = {
            'post': post,
            'comments': comments,
            'comment_form': CommentForm(),
            'profile': request.user.profile,
        }
        return render(request, 'posts/view_post.html', context)
