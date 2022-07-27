from django.shortcuts import render
from django.views import View

def get_home(request):
  return render(request, 'home/index.html')
