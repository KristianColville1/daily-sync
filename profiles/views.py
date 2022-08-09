from django.shortcuts import render
from django.views import View
from .models import Profile
from posts.models import Post


class ProfileOwnerView(View):
    """
    ProfileOwnerView class renders a users profile
    """

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(author=request.user)
        context = {
            'profile': Profile(),
            'posts': post
        }
        return render(request, 'profiles/index.html', context)
