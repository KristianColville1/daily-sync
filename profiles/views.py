from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import Profile
from posts.models import Post
from posts.forms import CommentForm, PostForm


class ProfileOwnerView(View):
    """
    ProfileOwnerView class renders a oweners profile
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(author=request.user)
        profiles = Profile.objects.exclude(user=request.user)
        post_paginator = Paginator(post, 10)
        page_number = request.GET.get('page')
        post_obj = post_paginator.get_page(page_number)
        profile_paginator = Paginator(profiles, 5)
        page_number = request.GET.get('page')
        profile_obj = profile_paginator.get_page(page_number)
        context = {
            'profile': request.user.profile,
            'profiles': profile_obj,
            'posts': post_obj,
            'comment_form': CommentForm(),
            'form': PostForm()
        }
        return render(request, 'profiles/index.html', context)


class ProfileView(View):
    """
    ProfileView class renders generic user profile view
    """
    def get(self, request, slug, *args, **kwargs):
        profile = get_object_or_404(Profile, slug=slug)
        context = {
            'profile': profile,
        }
        return render(request, 'profiles/user_profiles.html', context)


class ProfilesView(View):
    """
    ProfilesView class renders all users profiles
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(author=request.user)
        context = {'profile': request.user.profile, 'posts': post}
        return render(request, 'profiles/user_profiles.html', context)
