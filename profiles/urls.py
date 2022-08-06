from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileOwnerView.as_view(), name='profile'),
]
