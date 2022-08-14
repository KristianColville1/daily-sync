from django.shortcuts import render
from django.views import View
from posts.models import Post
from posts.forms import CommentForm, PostForm


class ProfileOwnerView(View):
    """
    ProfileOwnerView class renders a users profile
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(author=request.user)
        context = {
            'profile': request.user.profile,
            'posts': post,
            'comment_form': CommentForm(),
            'form': PostForm()
        }
        return render(request, 'profiles/index.html', context)


class ProfilesView(View):
    """
    ProfilesView class renders all users profiles
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(author=request.user)
        context = {'profile': request.user.profile, 'posts': post}
        return render(request, 'profiles/user_profiles.html', context)
