from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator
from .models import Profile
from posts.models import Post
from posts.forms import CommentForm, PostForm


class ProfileOwnerView(View):
    """
    ProfileOwnerView class renders a owners profile
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(author=request.user)
        profiles = Profile.objects.exclude(follows=request.user.profile)
        post_paginator = Paginator(post, 10)
        page_number = request.GET.get('page')
        post_obj = post_paginator.get_page(page_number)
        profile_paginator = Paginator(profiles, 5)
        profile_obj = profile_paginator.get_page(page_number)
        context = {
            'profile': request.user.profile,
            'profiles': profile_obj,
            'posts': post_obj,
            'comment_form': CommentForm(),
            'form': PostForm()
        }
        return render(request, 'profiles/index.html', context)


class OtherProfileView(View):
    """
    View another users profile
    """
    def get(self, request, slug, *args, **kwargs):
        user_profile = get_object_or_404(Profile, slug=slug)
        post = Post.objects.filter(author=user_profile.user)
        profiles = Profile.objects.exclude(follows=request.user.profile)
        post_paginator = Paginator(post, 10)
        page_number = request.GET.get('page')
        post_obj = post_paginator.get_page(page_number)
        profile_paginator = Paginator(profiles, 5)
        profile_obj = profile_paginator.get_page(page_number)
        context = {
            'profile': user_profile,
            'profiles': profile_obj,
            'posts': post_obj,
            'comment_form': CommentForm(),
            'form': PostForm()
        }
        return render(request, 'profiles/index.html', context)


class AllProfilesView(View):
    """
    ProfilesView class renders all users profiles
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(author=request.user)
        context = {'profile': request.user.profile, 'posts': post}
        return render(request, 'profiles/user_profiles.html', context)


# .............................................................. Function views
def follow_profile(request, profile_id):
    """
    follow profile adds user profile to following
    """
    profile = get_object_or_404(Profile, id=profile_id)
    profile.follows.add(request.user.profile)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def unfollow_profile(request, profile_id):
    """
    unfollow profile adds user profile to following
    """
    profile = get_object_or_404(Profile, id=profile_id)
    profile.follows.remove(request.user.profile)
    return redirect(request.META.get('HTTP_REFERER', '/'))
