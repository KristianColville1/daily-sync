from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileOwnerView.as_view(), name='profile'),
    path('user_profiles/', views.ProfilesView.as_view(), name='user_profiles'),
]
