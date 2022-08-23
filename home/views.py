from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

def get_home(request):
  if request.user.is_authenticated:
    return redirect('/feed/')
  return render(request, 'home/index.html')
