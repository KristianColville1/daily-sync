from django.shortcuts import render, get_object_or_404
from django.views import View
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
        context = {
            'profile': request.user.profile,
            'profiles': profiles,
            'posts': post,
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
