"""
Custom error handling for Daily Sync
"""
from django.shortcuts import render


def handler404(request, exception):
    """
    Renders the 404 page on errors
    """
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """
    Renders the 500 page on errors
    """
    return render(request, 'errors/500.html', status=500)