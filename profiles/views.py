from django.shortcuts import render
from django.views import View
from .models import Profile


class ProfileOwnerView(View):
    """
    ProfileView class renders a users profile
    """

    def get(self, request, *args, **kwargs):
        context = {
            'profile': Profile()
        }
        return render(request, 'profiles/index.html', context)
