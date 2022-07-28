from django.shortcuts import render
from django.views import View


def get_feed(request):
    return render(request, 'feed/index.html')
