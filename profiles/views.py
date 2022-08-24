from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from .models import FriendRequest, Profile
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


def add_friend(request, profile_id):
    from_user = request.user
    to_user = get_object_or_404(Profile, profile_id)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if created:
        messages.add_message(request, messages.SUCCESS,
                             'Your friend request was sent')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    messages.add_message(request, messages.SUCCESS,
                         'Oops! something went wrong please try again')
    return redirect(request.META.get('HTTP_REFERER', '/'))


def accept_friendship(request, friend_request_id, friendship):
    friend_request = FriendRequest.objects.get(id=friend_request_id)
    if friendship is True:
        friend_request.to_user.profile.friends.add(friend_request.from_user)
        friend_request.from_user.profile.friends.add(friend_request.to_user)
        friend_request.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        friend_request.not_accepted = True
        return redirect(request.META.get('HTTP_REFERER', '/'))